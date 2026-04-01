# Import Pretty Printing
from pprint import pprint

# Import the Nmap Module
import nmap3

# Create an nmap Object
nmap = nmap3.Nmap()

# Helper functions

def print_output(message: str, results: str) -> None:
    """Handle output message and printing results"""
    pprint("")
    pprint('-'*30)
    pprint(message)
    pprint(results)


# Define target host
HOST = "10.0.0.5"
SUBNET = "10.0.0.0/24"

# TCP SYN scan example
results = nmap.scan_top_ports(HOST)
print_output(f"Top ports of {HOST}", results)

# Nmap OS Detection
results = nmap.nmap_os_detection(HOST)
print_output(f"OS detection for {HOST}", results)

# NSE subnet scan
results = nmap.nmap_subnet_scan(SUBNET)
print_output(f"Subnet scan for {SUBNET}", results)
