import socket
import ipaddress
import threading
import queue

def is_port_open(ip, port, timeout=0.5):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        return True
    except:
        return False
    finally:
        s.close()

def scan_port(ip, port, open_ports_dict, dict_lock):
    if is_port_open(ip, port):
        with dict_lock:
            if ip in open_ports_dict:
                open_ports_dict[ip].append(port)
            else:
                open_ports_dict[ip] = [port]

def ip_range(network):
    """Generate all IPs in a subnet."""
    return [str(ip) for ip in ipaddress.IPv4Network(network, strict=False)]

if __name__ == "__main__":
    target_subnet = input("Enter the subnet to scan (e.g., 192.168.1.0/24): ")
    start_port = int(input("Enter the start port number: "))
    end_port = int(input("Enter the end port number: "))

    print(f"Scanning subnet {target_subnet} for open ports...")

    open_ports_dict = {}
    dict_lock = threading.Lock()
    threads = []

    for ip in ip_range(target_subnet):
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(ip, port, open_ports_dict, dict_lock))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    for ip in open_ports_dict:
        print(f"{ip}[{', '.join(map(str, open_ports_dict[ip]))}]")

    print("Scanning completed.")
