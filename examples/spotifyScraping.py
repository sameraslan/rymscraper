import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'c480b13ef81c4e6aa0ab0119636eabe5'
secret = '50826f24c12044448b906de50ac74742'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_uri = '5LhTec3c7dcqBvpLRWbMcf'
track_uri = 'spotify:track:36apwMphkcaS63LY3JJMPh'
#album_uri = 'spotify:album:7GOdEIOvr41lvxDK7bvPrI'

sp.trace = False

# find album by name
album = "pink moon"
results = sp.search(q = "album:" + album, type = "album")

# get the first album uri
album_uri = results['albums']['items'][0]['uri']

# get album tracks
tracks = sp.album_tracks(album_uri)
for track in tracks['items']:
    print(track['name'])

results = sp.audio_features(album_uri)
print(results)
