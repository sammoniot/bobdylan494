import string

GENIUS_API_TOKEN='1eHSydZU6DqDROkteWbFhDQcZiuo8ncdHU4zmgTet2JAmnMJfl8ejnNI4uPSFwt5'
from lyricsgenius import Genius
from pathvalidate import sanitize_filename
import os
import re
def cleaner_file_name(filename):
    invalid_chars = r"\,<>:\’\’\'/\|\?\*"
    filename= re.sub(invalid_chars,"",filename)
    filename= re.sub("\s","_",filename)
    return filename
genius = Genius(GENIUS_API_TOKEN)
artist = genius.search_artist("Bob Dylan", max_songs=3, sort="title")
print(artist.songs)

album = genius.search_album("The Frewheelin' Bob Dylan", "Bob Dylan")

for track in album.tracks:
    file_name = track.song.title + ".txt"
    cleaned_file_name = cleaner_file_name(sanitize_filename(file_name))
    print("Downloading file: " +cleaned_file_name)
    with open(cleaned_file_name, 'w', encoding="utf-8") as f:
        f.write(track.song.lyrics)
    #print(track.song.lyrics)

# album.save_lyrics()