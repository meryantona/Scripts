#!/usr/bin/env python3
import requests
import feedparser
import sys
from datetime import datetime

def clear_terminal():
    """Clear the terminal screen."""
    import os
    os.system('clear')

def fetch_google_news_spain():
    # URL of the Google News RSS feed for Spain
    url = "https://news.google.com/rss?hl=es&gl=ES&ceid=ES:es"

    try:
        # Fetching the RSS feed
        response = requests.get(url)

        # Parse the RSS feed
        feed = feedparser.parse(response.text)

        # Extracting news titles and URLs
        news_articles = []
        for entry in feed.entries:
            news_articles.append({"title": entry.title, "url": entry.link})

        return news_articles

    except Exception as e:
        print("An error occurred while fetching or parsing the RSS feed:", e)
        return []

def main():
    # Clear the terminal screen
    clear_terminal()

    # Print banner and current date/time
    print("\033[1;33m")  # Orange and Bold
    print("*** Noticias RSS Google News Espa\u00f1a ***")
    print("Fecha y hora:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("\033[0m")  # Reset color
    print()

    # Fetch news articles
    news_articles = fetch_google_news_spain()

    # Printing news titles and URLs
    if not news_articles:
        print("No news articles found.")
    else:
        for index, article in enumerate(news_articles, start=1):
            title = "\033[1;34m" + article['title'] + "\033[0m"  # Bold and blue for title
            url_text = "\033[1;33mURL: \033[0m"  # Orange and Bold for URL text
            print(f"{index}. {title}")
            print(f"   {url_text} {article['url']}\n")

if __name__ == "__main__":
    main()
