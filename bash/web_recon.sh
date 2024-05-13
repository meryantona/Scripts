#!/bin/bash
# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to display banners
display_banner() {
    echo -e "${GREEN}"
    echo " Simple Web Recon Script -  "
    echo " DNS Enumeration, WHOIS Look Up, Port Scanning "
    echo " WebServer Information(HTTP) #add https"
    echo " SSL Certificate Information(HTTPS)"
    echo " Robots.txt(HTTP) #change to https"
    echo " Directory Listing (HTTP+HTTPS)"
    echo -e "${NC}"
    echo -e "${YELLOW}--- Website Security Recon Script ---${NC}"
    echo ""
}

display_banner

# Get user input for IP or domain
read -p "Enter IP or domain: " target

# Check if user provided an IP or domain
if [ -z "$target" ]; then
    echo -e "${RED}Invalid input. Please provide an IP or domain.${NC}"
    exit 1
fi

# Step 1: DNS Enumeration
echo -e "${YELLOW}Performing DNS Enumeration...${NC}"
host "$target"
nslookup "$target"
echo ""

# Step 2: WHOIS Lookup
echo -e "${YELLOW}Performing WHOIS Lookup...${NC}"
whois "$target"
echo ""

# Step 3: Port Scanning
echo -e "${YELLOW}Performing Port Scanning...${NC}"
nmap -sC -sV "$target"
echo ""

# Step 4: Web Server Information (HTTP)
echo -e "${YELLOW}Fetching Web Server Information (HTTP)...${NC}"
curl -I "http://$target" 2>/dev/null | head -n 1
echo ""

# Step 5: SSL Certificate Information (HTTPS)
echo -e "${YELLOW}Fetching SSL Certificate Information (HTTPS)...${NC}"
openssl s_client -showcerts -connect "$target:443" </dev/null 2>/dev/null | openssl x509 -noout -text
echo ""

# Step 6: Robots.txt Check (HTTP)
echo -e "${YELLOW}Checking for robots.txt (HTTP)...${NC}"
curl -s "http://$target/robots.txt"
echo ""

# Step 7: Directory Listing Check (HTTP)
echo -e "${YELLOW}Checking for Directory Listing (HTTP)...${NC}"
response=$(curl -s -o /dev/null -w "%{http_code}" "http://$target/")
if [ "$response" -eq 200 ]; then
    echo "Directory listing is enabled."
else
    echo "Directory listing is not enabled. Attempting directory brute-forcing..."
    dirb "http://$target" /usr/share/wordlists/dirb/common.txt
fi
echo ""

# Step 8: Directory Listing Check (HTTPS)
echo -e "${YELLOW}Checking for Directory Listing (HTTPS)...${NC}"
response=$(curl -s -o /dev/null -w "%{http_code}" "https://$target/")
if [ "$response" -eq 200 ]; then
    echo "Directory listing is enabled."
else
    echo "Directory listing is not enabled. Attempting directory brute-forcing..."
    dirb  "https://$target" /usr/share/wordlists/dirb/common.txt
fi
echo ""
