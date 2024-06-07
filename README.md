## Web Scraper

This web scraper utilizes the `requests` library and `BeautifulSoup4` to extract data from the top players listed on the page [GPlay Dota Premium Ladder](https://www.gplay.gg/client/ladder/dota/premium).

### What I Learned

- **Understanding Site Structure**: It's crucial to analyze the HTML structure of the website to properly select the elements you want to extract. In this project, I identified the players and their corresponding points by examining the HTML structure. Once identified, I used the `get_text(strip=True)` method to extract the text content while stripping away any unnecessary characters, enabling me to retrieve the desired information efficiently.
