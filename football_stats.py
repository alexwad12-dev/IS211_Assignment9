import requests
from bs4 import BeautifulSoup

url = "https://www.cbssports.com/nfl/stats/player/receiving/nfl/regular/all/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

rows = table.find_all("tr")

print("Top 20 players:\n")
for row in rows[1:21]: # only want the top twenty
    cells = row.find_all("td")
    if len(cells) >= 8:
        player = cells[0].get_text(strip=True)
        team = cells[1].get_text(strip=True)
        pos = cells[2].get_text(strip=True)
        touchdowns = cells[7].get_text(strip=True)
        print(f"{player:<25} | {team:<4} | {pos:<3} | TD: {touchdowns}")

if __name__ == "__main__":
    print("Running scrapper one...")