# Task 6 – Web Scraping from Books Website

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

books = soup.find_all("h3")

print("\n--- Top 5 Books from website ---\n")
for b in books[:5]:
    title = b.find("a")["title"]
    print(title)
