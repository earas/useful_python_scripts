import sys
import socket
import ipaddress
import threading
from contextlib import closing
from queue import Queue

# Set a default timeout value
DEFAULT_TIMEOUT = 1

def is_port_open(ip, port, timeout=DEFAULT_TIMEOUT):
    try:
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((str(ip), port))
            return result == 0
    except socket.error as e:
        print(f"Error checking {ip}:{port}, {e}")
        return False

def check_subnet(subnet, port, timeout, only_open):
    for ip in subnet.hosts():
        if is_port_open(ip, port, timeout):
            print(f"Port {port} on {ip} is open.")
        elif not only_open:
            print(f"Port {port} on {ip} is closed.")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python port_check_multiple_subnets.py <port> [only_open]")
        sys.exit(1)

    port = int(sys.argv[1])
    only_open = len(sys.argv) == 3 and sys.argv[2].lower() == 'only_open'

    ip_networks = [
       "192.168.1.0/24",
       "10.0.0.0/24",
       "172.16.0.0/24",
       "192.168.2.0/24",
       "10.0.1.0/24"
    ]

    threads = []
    for ip_network in ip_networks:
        subnet = ipaddress.ip_network(ip_network, strict=False)
        print(f"Checking IP network: {ip_network}")

        thread = threading.Thread(target=check_subnet, args=(subnet, port, DEFAULT_TIMEOUT, only_open))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
