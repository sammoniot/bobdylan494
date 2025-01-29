import string


import config
genius_token = config.GENIUS_API_TOKEN
from lyricsgenius import Genius
from pathvalidate import sanitize_filename
import os
import re
target_folder = r"C:\Users\sammo\OneDrive\Desktop\digit494\bobdylan494\lyrics-txt\earlydylan\thefreewhelinbobdylan"

if not os.path.exists(target_folder):
    os.makedirs(target_folder)
def cleaner_file_name(filename):
    invalid_chars = r"[,<>:\’\’\'/\|\?\*]"
    filename= re.sub(invalid_chars,"",filename)
    filename= re.sub("\s","_",filename)
    return filename
def clean_lyrics(text):
    if text:
        text = re.sub(r"\d+\s+Contributors", "", text)
        text = re.sub(r"See Bob Dylan Live.*?\$\d+.*", "", text, flags=re.DOTALL)
    return text.strip()
    return ""

genius = Genius(genius_token)
artist = genius.search_artist("Bob Dylan", max_songs=3, sort="title")
print(artist.songs)

album = genius.search_album("The Freewhelin' Bob Dylan", "Bob Dylan")

for track in album.tracks:
    file_name = track.song.title + ".txt"
    cleaned_file_name = cleaner_file_name(sanitize_filename(file_name))
    file_path = os.path.join(target_folder, cleaned_file_name)
    print("Downloading file: " + cleaned_file_name)
    cleaned_lyrics = re.sub(r"\d+\s*Contributors", "", track.song.lyrics)
    lyrics = track.song.lyrics  # Ensure lyrics are fetched
    cleaned_lyrics = clean_lyrics(lyrics)

    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(cleaned_lyrics)
    #print(track.song.lyrics)

# album.save_lyrics()