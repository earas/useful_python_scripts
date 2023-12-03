# Python Brute Force Password Cracker

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


