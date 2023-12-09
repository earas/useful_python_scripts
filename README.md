# 1) Brute Force Linux Password

This Python script is a brute force password cracker that uses multiprocessing to attempt to find a password based on a given hash. It's designed to be a simple demonstration of brute force techniques in Python, specifically targeting password hashes commonly found in the `/etc/shadow` file on Linux systems.

## Understanding the `/etc/shadow` File

In Linux, the `/etc/shadow` file stores secure user account information, including encrypted passwords. Each line in the file represents an account and follows this structure:

| Field                | Example          | Description                                          |
|----------------------|------------------|------------------------------------------------------|
| Username             | `ekrem`           | User's login name.                                   |
| Encrypted Password   | `$6$.n.:...`     | The password hash with the algorithm identifier/salt. |
| Last Password Change | `17736`          | Days since Jan 1, 1970, that the password was changed.|
| Minimum Password Age | `0`              | Minimum number of days allowed between password changes.|
| Maximum Password Age | `99999`          | Maximum number of days the password is valid.        |
| Password Warning Period | `7`           | Days before password expiry to warn the user.        |
| Password Inactivity Period | ` `         | Days after password expiry until account is disabled.|
| Account Expires      | ` `              | Days since Jan 1, 1970, that the account is disabled.|
| Unused               | ` `              | Reserved for future use.                             |

For example, a line in `/etc/shadow` might look like this:

ekrem:$6$.n.:17736:0:99999:7:::
ekrem:$6$I2kBTChku9dL40Yg$N5XibbECwrHl5DyA232qiybPZ94gFNgdh4mw8FHhSpVGgbKTEdn10yA.u3gFTeCo2p868lb8FnNWMzqH5AAc81:17736:0:99999:7:::
Format: `$[algorithm_id]$[salt]$[hashed_password]`
$6  $I2kBTChku9dL40Yg  $N5XibbECwrHl5DyA232qiybPZ94gFNgdh4mw8FHhSpVGgbKTEdn10yA.u3gFTeCo2p868lb8FnNWMzqH5AAc81


### Hashing Algorithm Identifiers

The encrypted password segment starts with an algorithm identifier, which is indicative of the hash type used:

- `$1$`: MD5
- `$2a$` / `$2y$`: Blowfish
- `$5$`: SHA-256
- `$6$`: SHA-512
- `$y$`: yescrypt

## Features

- Utilizes `multiprocessing` for faster execution.
- Customizable character set and password length.
- Estimates and displays the total number of possible combinations.
- Calculates and displays the estimated maximum time for the operation.
- Displays execution time upon completion.
- Can be modified for various hashing algorithms supported by Python's `crypt` module.

## How to Use

1. **Clone the repository:**
   Clone this repository to your local machine using `git clone`.

2. **Set Up Your Environment:**
   Ensure you have Python installed. This script was tested with Python 3.8. No additional libraries are required beyond the Python standard library.

3. **Configure the Script:**
   - Set the `target_hash` variable to the hash you want to crack.
   - Set the `salt` variable if required by the hashing algorithm.
   - Adjust the `characters` list to the set of characters you want to include in the password search.
   - Set `password_length` to the length of the password you're trying to crack.
   - Adjust `num_processes` based on the number of CPU cores you want to utilize.

4. **Run the Script:**
   Execute the script using Python:

   ```bash
   python brute_force_linux_password.py


### Disclaimer
This script is for educational purposes only. Unauthorized password cracking or hacking is illegal and unethical.


# 2) Python Port Check Script

This script is designed to efficiently check for open network ports across multiple subnets using Python's multiprocessing capabilities. It's a practical tool for network administrators and security professionals to quickly assess network security and open ports.

## Features

- Checks multiple subnets for open ports.
- Uses threading for enhanced performance.
- Option to display only open ports for cleaner output.
- Handles timeouts and socket errors gracefully.
- Customizable through command-line arguments.

## Requirements

- Python 3.x
- Standard libraries: `sys`, `socket`, `ipaddress`, `threading`, `contextlib`

## Usage

To use the script, you need to specify the port you want to check. You can also optionally specify to only display open ports.

```bash
python port-check.py <port> [only_open]
```

- `<port>`: Required. The port number you want to check across the specified subnets.
- `[only_open]`: Optional. Include this argument to display only open ports.


### Example Commands

- To check both open and closed ports on port 80:
```bash
python port-check.py 80
```

- To check only open ports on port 80:
```bash
python port-check.py 80 only_open
```

## How It Works

The script iterates through predefined IP subnets, utilizing threading to check each IP within those subnets for the specified port's status. By default, it checks for both open and closed ports but can be configured to report only open ports.

## Customization

To customize the IP subnets checked, edit the `ip_networks` list in the script:

```python
ip_networks = [
 "192.168.1.0/24",
 "10.0.0.0/24",
 "172.16.0.0/24",
 "192.168.2.0/24",
 "10.0.1.0/24"
]
```
### Disclaimer
This script is intended for educational and legitimate professional use only. Unauthorized network scanning and port checking can be considered intrusive and illegal in many contexts. Always ensure you have explicit permission to scan the network in question.



# 3) IP Address Finder

This Python script is designed for extracting IP addresses from a text file. It's ideal for network administrators, security professionals, or anyone who needs to quickly and efficiently identify IP addresses in a document.

## Description

The script uses regular expressions to find and extract all occurrences of IP addresses from a given text file. It is efficient and easy to use, suitable for processing logs, network configurations, and other text files where IP addresses are listed.

## Getting Started

### Dependencies

- Python 3.x
- No external libraries are required.


## Features

- Extract IP addresses from any text file.
- Handles multiple IP addresses per line.
- Provides clear error messages for file not found or other issues.


### Using the Script

To use the script, simply run it with Python and pass the path of the text file as an argument:


```bash
python ip_finder.py
```

# 4) Port Range Scanner

A Python script for scanning a range of ports on all IP addresses within a given subnet. This tool is useful for network administrators and security professionals to identify open ports across multiple hosts.

## Description

The script utilizes multithreading to efficiently scan multiple ports on each IP address in a specified subnet. It reports the open ports for each IP address, aiding in network diagnostics and security audits.

## Getting Started

### Dependencies

- Python 3.x
- Standard libraries: `socket`, `ipaddress`, `threading`, `queue`


### Using the Script

Run the script with Python and follow the prompts to enter the subnet and port range:

```bash
python scanport-range.py
```


You will be asked to enter:
- Subnet to scan (e.g., `192.168.1.0/24`)
- Start port number
- End port number

The script will then scan the specified range and output the open ports for each IP address in the subnet.

## Features

- Scans all IPs within a specified subnet.
- Checks a specified range of ports for each IP.
- Utilizes multithreading for faster scanning.
- Reports open ports for each IP address.










