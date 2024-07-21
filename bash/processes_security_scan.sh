#!/bin/bash

# Define colors
BOLD=$(tput bold)
YELLOW=$(tput setaf 013)
BLUE=$(tput setaf 004)
GREEN=$(tput setaf 002)
RED=$(tput setaf 001)
BLINK=$(tput blink)
RESET=$(tput sgr0) # Reset formatting

# Clear the terminal
clear

# Print a header
echo "${BLUE}${BOLD}=========================================="
echo "Processes Scan: Another Practical Security Sweep"
echo "==========================================${RESET}"
echo ""

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to view system-level processes...${RESET}"

# Check system processes
echo "${GREEN}${BOLD}System-Level Processes:${RESET}"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
echo ""
read -p "${YELLOW}Press [Enter] to view user-specific processes...${RESET}"

# Check user-specific processes
echo "${GREEN}${BOLD}User-Level Processes:${RESET}"
ps -u $(whoami) -o pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
echo ""
read -p "${YELLOW}Press [Enter] to view hierarchical process list...${RESET}"

# Check hierarchical process list
echo "${GREEN}${BOLD}Hierarchical Process List:${RESET}"
ps -eFH
echo ""
read -p "${YELLOW}Press [Enter] to view detailed process information...${RESET}"

# Detailed process information
echo "${GREEN}${BOLD}Detailed Process Information:${RESET}"
ps aux --sort=-%mem | head -n 15
echo ""
read -p "${YELLOW}Press [Enter] to finish the scan...${RESET}"

# Finishing statement
echo "${BLUE}${BOLD}=========================================="
echo "Processes Scan Completed"
echo "==========================================${RESET}"
