import sqlite3
import json
from types import SimpleNamespace

class Song:
        def __init__(self, title, timeListened, artist, album, msplayed):
                self.title = title
                self.artist = artist
                self.album = album
                self.timeListened = timeListened
                self.msplayed = msplayed



def parseData(filename):

    with open(filename, 'r') as file:
           list = json.load(file)

    songs = []

    for entry in list:
           
        if entry["master_metadata_track_name"] == None:
            continue

        song = Song(
                  
                title=entry["master_metadata_track_name"],
                artist=entry["master_metadata_album_artist_name"],
                album=entry["master_metadata_album_album_name"],
                timeListened=entry["ts"],
                msplayed=entry["ms_played"]

            )
        
        songs.append(song)

        return songs

conn = sqlite3.connect("myData.db")

cursor = conn.cursor()

cursor.execture("""
CREATE TABLE IF NOT EXISTS songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT
    artist TEXT
    album TEXT
    time_listened TEXT
    ms_played INTEGER
    )
""")
conn.commit()

if __name__ == "__main__":
    filename = input(string("Enter the filename: "))
    parseData(filename)

