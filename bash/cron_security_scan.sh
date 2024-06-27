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
echo "Cron Jobs Scan: A Practical Security Sweep"
echo "==========================================${RESET}"
echo ""

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to view system-level crontab entries...${RESET}"

# View system-level crontab entries
echo "${GREEN}${BOLD}System-level Crontab Entries:${RESET}"
echo ""
echo "-----Contents of main cron tab file /etc/crontab:-----"
sudo cat /etc/crontab
echo ""

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to view files in /etc/cron.d...${RESET}"

# Check cron jobs in /etc/cron.d
echo "${GREEN}${BOLD}Listing Files in /etc/cron.d:${RESET}"
echo ""
sudo ls -l /etc/cron.d
for file in /etc/cron.d/*; do
    echo ""
    echo "${BLUE}-----Contents of $file:-----${RESET}"
    echo ""
    sudo cat "$file"
    echo ""
done

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to view periodic cron directories...${RESET}"

# Check cron.daily, cron.hourly, cron.monthly, and cron.weekly
for dir in /etc/cron.daily /etc/cron.hourly /etc/cron.monthly /etc/cron.weekly; do
    echo ""
    echo "${GREEN}${BOLD}Listing Files in $dir:${RESET}"
    echo ""
    sudo ls -l "$dir"
    for file in "$dir"/*; do
        echo ""
        echo "${BLUE}-----Contents of $file:-----${RESET}"
        echo ""
        sudo cat "$file"
        echo ""
    done
done

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to view crontab entries for specific users...${RESET}"

# View crontab entries for specific users
echo "${GREEN}${BOLD}Crontab Entries for Root:${RESET}"
echo ""
echo "-----Contents of crontab for user Root:-----"
sudo crontab -l -u root
echo ""

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to view crontab entries for all users...${RESET}"

# Check user-specific cron jobs
echo "${GREEN}${BOLD}User-specific Crontab Entries:${RESET}"
for user in $(cut -f1 -d: /etc/passwd); do
    echo "${BLUE}-----Cron jobs for user: $user-----${RESET}"
    sudo crontab -u "$user" -l 2>/dev/null
    echo ""
done

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to check for unauthorized crontab files...${RESET}"

# Check for unauthorized crontab files
echo "${GREEN}${BOLD}Listing Crontab File:${RESET}"
echo ""
echo "-----Contents of /var/spool/cron/crontabs/:-----"
sudo ls /var/spool/cron/crontabs/
echo ""

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to check system logs for suspicious cron entries...${RESET}"

# Check system logs for suspicious cron entries
echo "${GREEN}${BOLD}Checking System Logs:${RESET}"
echo ""
echo "-----Contents of /var/log/syslog:-----"
sudo grep "CRON" /var/log/syslog | tail -n 20
echo ""

# Pause for the user to read
read -p "${YELLOW}Press [Enter] to exit...${RESET}"
echo ""

# Print a footer
echo "${BLUE}${BOLD}======================="
echo "Scan Complete"
echo "=======================${RESET}"
echo ""
