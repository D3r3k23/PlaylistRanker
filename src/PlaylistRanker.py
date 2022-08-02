import lastfmget

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotify.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='',
    client_secret=''
))

from dataclasses import dataclass
from enum import Enum

playlistURL = ""

class DataType(Enum):
    Track  = 0
    Artist = 1
    Album  = 2

    def __str__(self):
        if self is DataType.Track:
            return 'Album'
        if self is DataType.Artist:
            return 'Artist'
        if self is DataType.Album:
            return 'Album'

@dataclass(eq=False)
class Song:
    """Contains information about a song"""
    title:  str
    artist: str
    album:  str

if __name__ == "__main__":

    songs = [] # Load from playlistURL

    scrobbles = [] # Load from LastFmApi

def get_songs(playlist):
    playlist = sp.get_playlist(url=playlistURL)
