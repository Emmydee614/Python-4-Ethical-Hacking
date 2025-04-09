# Import module
import socket
import argparse

# create a socket object
def scan_port(ip, port):
    """Check if a specific port is open on a given IP address."""
    try:
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # set a timeout for connection attempt
        s.settimeout(1)

        # Try connecting to the IP address and port 
        result = s.connect_ex((ip, port))

        # if condition statement 
        if result == 0:
            print(f"[+] port {port} is open on {ip}")
        else: 
            print(f"[-] port {port} is closed on {ip}")
        s.close()
    except Exception as e:
        print(f"[-] Error scannin port {port} on {ip}")


def scan_ports(ip, start_port, end_port):
    """scan a range of ports on a given ip address"""
    print(f"\n scanning {ip} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# The main program
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='this tool was created by webdeves cybersecurity student')
    parser.add_argument("ip", help="Target ip address")
    parser.add_argument("--start", type=int, default=1, help="specify starting port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="specify the ending port (default:1024)")

    args = parser.parse_args()


    scan_ports(args.ip, args.start, args.end)