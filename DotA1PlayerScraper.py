import requests
from bs4 import BeautifulSoup

def get_players(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")
    players = []

    rows = soup.find_all("tr")

    for row in rows:
        name_tag = row.find("a", href=True, )
        points_tag = row.find_all("td")

        if name_tag and points_tag:
            nickname = name_tag.get_text(strip=True)
            points = points_tag[2].get_text(strip=True)
            players.append({"name": nickname, "points": points })
    return players


def main():
    url = "https://www.gplay.gg/client/ladder/dota/premium"
    players = get_players(url)

    if not players:
        print("No players found")
        return

    with open("players.txt", "w", encoding="utf-8") as file:
        for player in players:
            file.write(f"{player['name']} - {player['points']} points\n")

    with open("players.txt", "r", encoding="utf-8") as file:
        print("Contents of the file:")
        print(file.read())

    print("Scraping complete. Data was saved to players.txt")


if __name__ == "__main__":
    main()
