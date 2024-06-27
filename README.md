A collection of homemade Scripts.

This collection of scripts serves various purposes, focusing on enhancing system functionalities, file modifications and web reconnaissance.

/// Python Scripts

➡️ news_google_spain_RSS.py

This script provides a simple yet effective way to fetch and display the latest news articles from the Google News RSS feed for Spain in the terminal. 
Links can be open directly in browser. 

➡️ web_scraping_all_links.py

This Python script allows users to input a domain name and fetch all the links from the corresponding web page. 
The extracted links are then displayed in the terminal and exported to a CSV file with the domain name as the filename. 
The script utilizes BeautifulSoup for HTML parsing and requests for making HTTP requests.

➡️ system_check.py

This script collects and displays system usage information, including CPU, memory, disk, network activity, and active connections. 
After retrieving the data, it prints the CPU usage, memory usage, and disk usage percentage, as well as information about network activity and active connections.


/// Bash Scripts

➡️ cron_security_scan.sh

This Bash script provides a comprehensive security scan of cron jobs on Linux systems. It systematically checks system-level and user-specific crontab entries, examines files in /etc/cron.d and periodic cron directories, looks for unauthorized crontab files, and reviews recent cron-related system logs.

➡️ mac_changer.sh

Bash script designed to change the MAC address of a specified network interface, restart the interface, and then check network connectivity.

1 - It checks if the macchanger utility is installed and if the script is being run with root privileges.

2 - It prompts the user to select a network interface to change the MAC address for.

3 - It restarts the network interface and tests network connectivity by pinging Google's DNS server (8.8.8.8).

➡️ web_recon.sh

This Bash script is designed for conducting basic reconnaissance on a given website or IP address. 

Features:

DNS Enumeration
WHOIS Lookup
Port Scanning
Web Server Information (HTTP)
SSL Certificate Information (HTTPS)
Robots.txt Check (HTTP)
Directory Listing Check (HTTP+HTTPS)


----------------------------
The scripts provided in this repository are intended for educational and informational purposes only. 
I do not assume any responsibility for the misuse, damage, or unauthorized use of these scripts. 
Users are solely responsible for their actions and should use these scripts responsibly and ethically in accordance with applicable laws and regulations.

Installation Requirements:

Please note that to ensure the proper functioning of the scripts, users may need to install additional tools or dependencies on their systems. 
These tools may vary depending on the script's functionality and requirements.

----------------------------






