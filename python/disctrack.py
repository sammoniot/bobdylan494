import config
from lyricsgenius import Genius
import csv

genius_token = config.GENIUS_API_TOKEN
genius = Genius(genius_token)
artist_id = 181

# def count_album_tracks(id):
#     album=genius.album_tracks(id)
#     print(album)


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
with open("disctrack.tsv","w",newline='') as f:
    writer = csv.writer(f,delimiter='\t')
    writer.writerow(["Album Title", "Album ID", "Track Count"])
for album in all_albums:
    album_id = album['id']
    album_data = genius.album_tracks(album_id) #different dict. needed for track information
    album_title = album['name']
    track_count = len(album_data['tracks'])
    #if album_data and 'tracks' in album_data:
        #track_count = len(album_data['tracks'])
    print(f"Number of tracks for {album_title} id {album_id} : {track_count}")
    writer.writerow([album_title, album_id, track_count])
with open("disctrack.tsv",newline='') as csvfile:
    data = csv.reader(csvfile, delimiter='\t')
    for row in data:
        print('\t'.join(row))