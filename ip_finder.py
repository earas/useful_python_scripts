import re

def extract_ips_from_file(file_path):
    # Regular expression pattern for matching IP addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Extracting IP addresses from each line
        for line in lines:
            # Find all matches of IP addresses in the line
            ip_addresses = re.findall(ip_pattern, line)
            
            # Print each IP address found
            for ip in ip_addresses:
                print(ip)

    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# Replace '/path/to/your/file.txt' with the path to your file
file_path = '/path/to/your/file.txt'
extract_ips_from_file(file_path)
