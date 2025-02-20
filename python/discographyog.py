import config
from lyricsgenius import Genius
import csv
genius_token = config.GENIUS_API_TOKEN
genius = Genius(genius_token)
artist_id = 181  # Example ID; change this as needed
all_albums = []
page = 1
while True:
    albums_data = genius.artist_albums(artist_id, per_page=50, page=page)  # Increase per_page if needed
    if not albums_data or 'albums' not in albums_data:
        break
    albums_list = albums_data['albums']  # Extract the actual list of albums

    if not albums_list:  # Stop if there's no album data
            break
    all_albums.extend(albums_list)
    if 'next_page' not in albums_data or not albums_data['next_page']:  # Check if more pages exist
        break
    page += 1

albums_data = genius.artist_albums(artist_id)
#print(albums_data)
#print(all_albums)
# Ensure we got a valid response
data = []
for album in all_albums:
    album_title = album.get('name') or album.get('title', 'Unknown Title')  # Some versions use 'title' instead of 'name'
    album_date = album.get('release_date_for_display', 'Unknown Year')  # Safely get the release year
    album_components = album.get('release_date_components', {})  # Get the nested dict safely
    #print(album_components)
    if album_components is not None:
        album_year = album_components.get('year')
    else: album_year = None
    #print(album_year)
    data.append([album_title, album_date, album_year])
print(data)
#print(f"{album_title} ({album_year})")
with open("discography1.tsv","w",newline='') as f:
    writer = csv.writer(f,delimiter='\t')
    writer.writerows(data)
with open("discography1.tsv",newline='') as csvfile:
    data = csv.reader(csvfile, delimiter='\t')
    for row in data:
        print('\t'.join(row))
