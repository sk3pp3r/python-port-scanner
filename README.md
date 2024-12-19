# Port Scanner

A simple port scanner written in Python. This tool can be used to scan a range of ports on a specified IP address to determine which ports are open.

## Features

- Scans a range of ports on a target IP address.
- Identifies open ports within the specified range.
- Provides the duration of the scan.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository:**

    ```sh
    git clone https://github.com/sk3pp3r/python-port-scanner.git
    cd python-port-scanner
    ```

2. **Run the port scanner:**

    ```sh
    python port_scanner.py
    ```

3. **Follow the prompts to enter the target IP address and port range:**

    ```sh
    Enter the IP address to scan: 192.168.1.1
    Enter the start port: 1
    Enter the end port: 1024
    ```

4. **View the results:**

    The script will display the open ports and the time taken to complete the scan.

## Example Output

```sh
Enter the IP address to scan: 192.168.1.1
Enter the start port: 1
Enter the end port: 1024
Scanning ports on 192.168.1.1 from 1 to 1024...
Scanning completed in 0:00:15.123456
Open ports: [22, 80, 443]
