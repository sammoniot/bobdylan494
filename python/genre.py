import requests
import csv
from bs4 import BeautifulSoup



URL = "https://bobdylan.fandom.com/wiki/Discography"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html.parser')
#all_albums = []
album_url = [a['href'] for a in soup.find_all('a',href=True,title=True)]
#print(album_url)
a = soup.find_all('a')
album_title =[a['title']]
for a in  soup.select('a[data-tracking="custom-level-3"]'):
    print(album_title.text)
genre = soup.select_one('div[data-source="genre"]')
print(genre)
a_tag = soup.find('a', href="/wiki/Bob_Dylan")
if a_tag:
    li_element = a_tag.find_parent('li')  # Get the parent <li> element
    if li_element:
        role_text = li_element.text.strip()
        #print(li_element.text.strip())
   # print(a_tag.text)


#div_tag = soup.select_one('div[data-source="genre"]')
#genre_div = div_tag.select_one('div')
#print(genre_div.text)

