#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_user_input():
    """Prompt the user to enter a URL."""
    url = input("Enter the domain (e.g., example.com): ").strip()
    return url

def fetch_links(url):
    """Fetch links from the specified URL."""
    try:
        # Add 'https://' to the URL if it's missing
        if not urlparse(url).scheme:
            url = 'https://' + url

        # Fetch the web page
        page = requests.get(url)
        page.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(page.content, "html.parser")

        # Find all the links on the page
        links = soup.find_all("a")

        return links

    except requests.RequestException as e:
        print("Error fetching the web page:", e)
        return []

def display_links(links):
    """Display links in the terminal."""
    print("Links found on the page:")
    for link in links:
        print(link.get("href"))

def export_links_to_csv(links, domain):
    """Export links to a CSV file."""
    try:
        # Construct the CSV file name
        csv_file_name = f"{domain}_links.csv"

        # Open the CSV file in write mode
        with open(csv_file_name, "w", newline="", encoding="utf-8") as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)

            # Write header row
            csv_writer.writerow(["Link"])

            # Write each link to the CSV file
            for link in links:
                csv_writer.writerow([link.get("href")])

        print(f"Links exported to {csv_file_name}")

    except Exception as e:
        print("Error exporting links to CSV:", e)

def main():
    # Get user input for the domain
    domain = get_user_input()

    # Fetch links from the specified URL
    links = fetch_links(f"https://{domain}")

    # Display links in the terminal
    if links:
        display_links(links)

    # Export links to a CSV file
    if links:
        export_links_to_csv(links, domain)

if __name__ == "__main__":
    main()
