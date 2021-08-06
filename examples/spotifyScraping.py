import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'c480b13ef81c4e6aa0ab0119636eabe5'
secret = '50826f24c12044448b906de50ac74742'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_uri = '5LhTec3c7dcqBvpLRWbMcf'
track_uri = 'spotify:track:36apwMphkcaS63LY3JJMPh'

results = spotify.audio_features(track_uri)
print(results)
