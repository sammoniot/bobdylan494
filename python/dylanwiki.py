import requests
import csv
from bs4 import BeautifulSoup
from lxml import html

URL = "https://bobdylan.fandom.com/wiki/Discography"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

def readlink(album_link):
    fullURL = "https://bobdylan.fandom.com" + album_link
    af = requests.get(fullURL).content
    tree = html.fromstring(af)
    title = tree.xpath('//h2[@data-source="title1"]/text()')
    recordedDate = tree.xpath('//div[@data-source="recorded"]/div/text()')
    releaseDate = tree.xpath('//div[@data-source="released"]/div/text()')
    format = tree.xpath('//div[@data-source="format"]/div/text()')
    studio = tree.xpath('//div[@data-source="studio"]/div/text()')
    genre = tree.xpath('//div[@data-source="genre"]/div/text()')
    length = tree.xpath('//div[@data-source="length"]/div/text()')
    producer = tree.xpath('//div[@data-source="producer(s)"]/div/text()')
    instruments = tree.xpath('//li[a[@href="/wiki/Bob_Dylan"]]/text()')
    print(f"Album: {title}, URL: {fullURL}, Recorded Date {recordedDate}, Release Date: {releaseDate}, "
          f"Length: {length}, Format: {format}, Studio: {studio}, Genre: {genre}, Producer: {producer}, "
          f"Instruments, {instruments}")
    writer.writerow([album_title, fullURL, recordedDate, releaseDate, format, studio, genre, length, producer, instruments])


# Open the file for writing
with open("dylanwiki-FullAlbumData.tsv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(["Album Title", "URL","Recorded", "Released", "Format", "Studio", "Genre", "Length", "Producer", "Instrumentation"])

    # Find all rows in the table
    for row in soup.find_all('tr'):
        tds = row.find_all('td')

        if len(tds) >= 3:
            a_tag = tds[1].find('a')

            if a_tag and 'title' in a_tag.attrs:
                album_title = a_tag.attrs['title']
                length = tds[2].text.strip()
                album_link = a_tag.attrs['href']
                readlink(album_link)

