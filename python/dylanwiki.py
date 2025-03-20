import requests
import csv
from bs4 import BeautifulSoup

URL = "https://bobdylan.fandom.com/wiki/Discography"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

# Open the file for writing
with open("dylanwiki2.tsv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(["Album Title", "Length"])

    # Find all rows in the table
    for row in soup.find_all('tr'):
        tds = row.find_all('td')

        if len(tds) >= 3:
            a_tag = tds[1].find('a')

            if a_tag and 'title' in a_tag.attrs:
                album_title = a_tag.attrs['title']
                length = tds[2].text.strip()

                print(f"Album: {album_title}, Length: {length}")
                writer.writerow([album_title, length])
print(soup.prettify())
print(r.content)
