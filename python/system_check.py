#!/usr/bin/env python3

import shutil
import psutil

# Function to display network interface information
def display_network_info(io_counters):
    print("**Network Activity:**\n")
    for interface, counters in io_counters.items():
        print(f"Interface {interface}:")
        print(f"  Bytes Sent: {counters.bytes_sent}")
        print(f"  Bytes Received: {counters.bytes_recv}")
    print()

# Function to display active connections
def display_active_connections(connections):
    print("**Active Connections:**\n")
    for connection in connections:
        local_addr = connection.laddr or "N/A"
        remote_addr = connection.raddr or "N/A"
        status = connection.status
        print(f"Local Address: {local_addr[0]}:{local_addr[1]} <-> Remote Address: {remote_addr[0]}:{remote_addr[1]} ({status})")
    print()

# Function to display system usage information
def display_system_usage(cpu_usage, memory_usage, percent_used):
    print("**System Usage:**\n")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")
    print(f"Disk Usage: {percent_used:.2f}%")

# Get the current CPU usage
cpu_usage = psutil.cpu_percent()

# Get the current memory usage
memory_usage = psutil.virtual_memory().percent

# Get the disk usage
disk_usage = shutil.disk_usage("/")
total_space = disk_usage.total
used_space = disk_usage.used
percent_used = (used_space / total_space) * 100

# Get the network activity
# Get the current input/output data rates for each network interface
io_counters = psutil.net_io_counters(pernic=True)

# Get a list of active connections
connections = psutil.net_connections()

# Display network interface information
display_network_info(io_counters)

# Display active connections
display_active_connections(connections)

# Display system usage information
display_system_usage(cpu_usage, memory_usage, percent_used)
