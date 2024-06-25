
# SSH Cracker

## Overview
SSH Cracker is a professional tool designed for ethical penetration testing and security assessments Develops by LordSMH. It attempts to brute-force SSH credentials using a combination of usernames and passwords while optionally routing traffic through a list of proxies to avoid detection and IP bans.

## Features
- **Multi-threading/Parallel Processing**: Uses concurrent threads to speed up the cracking process.
- **Customizable Wordlists**: Supports external files for username and password lists.
- **Proxy Support**: Allows routing through a list of proxies to avoid IP bans.
- **Configurable Connection Timeout**: Adjustable timeout settings for SSH connections.
- **Logging and Reporting**: Provides detailed logs of the cracking process.
- **Session Management and Reattempt Logic**: Stops further attempts upon the first successful login.
- **User-friendly Command Line Interface (CLI)**: Easy-to-use CLI for specifying options and inputs.

## Installation
To get started, clone the repository and install the required dependencies.

### Clone the Repository
```sh
git clone https://github.com/lordsmh/ssh-cracker.git
cd ssh-cracker
```

### Install Dependencies
Install the required Python packages using `pip`:

```sh
pip install -r requirements.txt
```

## Usage
To use SSH Cracker, you need to provide a target host, port, username list, password list, and optionally a proxy list. Below is an example command to run the script:

```sh
python ssh_cracker.py target_host 22 usernames.txt passwords.txt --proxy-list proxies.txt --max-workers 20 --timeout 10
```

### Arguments
- `host`: Target hostname or IP address.
- `port`: Target SSH port (usually 22).
- `usernames`: File containing list of usernames.
- `passwords`: File containing list of passwords.
- `--max-workers`: Maximum number of concurrent threads (default: 10).
- `--timeout`: Connection timeout in seconds (default: 5).
- `--proxy-list`: File containing list of proxies (optional).

### Example Files
- **usernames.txt**:
    ```
    admin
    root
    user
    ```

- **passwords.txt**:
    ```
    password
    123456
    admin
    ```

- **proxies.txt**:
    ```
    103.25.155.53:83
    178.62.193.19:53281
    89.218.133.170:3128
    ```

## Example
Running SSH Cracker with a target host, username list, password list, and proxy list:
```sh
python ssh_cracker.py example.com 22 usernames.txt passwords.txt --proxy-list proxies.txt --max-workers 20 --timeout 10
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Disclaimer
This tool is intended for educational purposes and ethical penetration testing only. Unauthorized use of this tool to access or damage any system without explicit permission is illegal and unethical. Use responsibly.

## Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

## Contact
For any questions or issues, H4ckL0rd5@gmail.com
