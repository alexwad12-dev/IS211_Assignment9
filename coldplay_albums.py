import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Coldplay_discography"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# Pass headers in the request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Get the first table
table = soup.find("table", {"class": "wikitable"})  # more specific

# Get all rows in that table
rows = table.find_all("tr")

# Loop through each row
for row in rows:
    # Find all <a> tags in that row (links)
    cells = row.find_all("a")
    for cell in cells:
        # Skip empty or anchor links
        text = cell.get_text(strip=True)
        if text and not text.startswith("#"):
            print(text)
