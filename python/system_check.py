#!/usr/bin/env python3
import os
import shutil
import socket
import sys
import psutil

# ANSI color codes
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    print("Checking for pending reboot...")
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there is enough free disk space, false otherwise."""
    print(f"Checking disk space on {disk}...")
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    return gigabytes_free < min_gb or percent_free < min_percent

def check_root_full():
    """Returns True if the root partition is full, False otherwise."""
    print("Checking if root partition is full...")
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    print("Checking network connectivity...")
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def display_network_info(io_counters):
    """Display network interface information."""
    print(f"\n{BLUE}Network Activity:{RESET}\n")
    for interface, counters in io_counters.items():
        print(f"Interface {interface}:")
        print(f"  Bytes Sent: {counters.bytes_sent}")
        print(f"  Bytes Received: {counters.bytes_recv}")
    print()

def display_active_connections(connections):
    """Display active connections."""
    print(f"{BLUE}Active Connections:{RESET}\n")
    for connection in connections:
        local_addr = connection.laddr or "N/A"
        remote_addr = connection.raddr or "N/A"
        status = connection.status
        print(f"Local Address: {local_addr[0]}:{local_addr[1]} <-> Remote Address: {remote_addr[0]}:{remote_addr[1]} ({status})")
    print()

def display_system_usage(cpu_usage, memory_usage, percent_used):
    """Display system usage information."""
    print(f"{BLUE}System Usage:{RESET}\n")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {percent_used:.2f}%")

def main():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = shutil.disk_usage("/")
    total_space = disk_usage.total
    used_space = disk_usage.used
    percent_used = (used_space / total_space) * 100
    io_counters = psutil.net_io_counters(pernic=True)
    connections = psutil.net_connections()

    print(f"\n{BLUE}Running system checks...{RESET}\n")
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full"),
        (check_no_network, "No working network"),
    ]
    everything_ok = True
    for check, msg in checks:
        print(f" - {msg}: ", end="")
        if check():
            print(f"{RED}FAIL{RESET}")
            everything_ok = False
        else:
            print(f"{GREEN}OK{RESET}")

    if not everything_ok:
        print(f"\n{RED}Some checks failed. Exiting with status code 1.{RESET}")
        sys.exit(1)

    print(f"\n{GREEN}System checks passed.{RESET}")

    display_network_info(io_counters)
    display_active_connections(connections)
    display_system_usage(cpu_usage, memory_usage, percent_used)

if __name__ == "__main__":
    main()
