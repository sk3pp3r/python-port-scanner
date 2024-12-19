# Python Port Scanner 
# Version 0.1a 
# Haim Cohen 2024

import socket
from datetime import datetime

# Function to scan a single port
def scan_port(ip, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout of 1 second
        result = sock.connect_ex((ip, port))  # Try to connect to the port
        sock.close()
        if result == 0:
            return True  # Port is open
        else:
            return False  # Port is closed
    except Exception as e:
        return False

# Function to scan a range of ports
def scan_ports(ip, start_port, end_port):
    print(f"Scanning ports on {ip} from {start_port} to {end_port}...")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    # Record the start time
    start_time = datetime.now()

    # Scan the ports
    open_ports = scan_ports(target_ip, start_port, end_port)

    # Record the end time
    end_time = datetime.now()

    # Calculate the duration
    duration = end_time - start_time

    # Print the results
    print(f"Scanning completed in {duration}")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")
