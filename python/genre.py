import requests
import csv
from bs4 import BeautifulSoup
URL = "https://bobdylan.fandom.com/wiki/Bob_Dylan_(album)"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
genre = soup.find('div', attrs={'data-source': 'genre'})
Genre =[]
if genre:
    divs = genre.find_all('div', attrs={'data-source': 'genre'})
    if genre:genre.find_parent('div', attrs={'data-source': 'genre'})
        genre