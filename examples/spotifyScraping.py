import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

cid = 'c480b13ef81c4e6aa0ab0119636eabe5'
secret = '50826f24c12044448b906de50ac74742'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_uri = '5LhTec3c7dcqBvpLRWbMcf'
track_uri = 'spotify:track:36apwMphkcaS63LY3JJMPh'
#album_uri = 'spotify:album:7GOdEIOvr41lvxDK7bvPrI'

df = pd.read_csv("Above1kRatings.csv")

#Albums deleted (not in spotify)
df = df.drop([54])  # King Crimson,The Great Deceiver: Live 1973-1974
df = df.drop([187])  # Joanna Newsom,Ys
df = df.drop([225])  # Electric Masada, At the Mountains of Madness
df = df.drop([239])  # Kraftwerk,Die Mensch-Maschine
df = df.drop([241])  # Shiro Sagisu,The End of Evangelion
df = df.drop([252])  # Les Rallizes dénudés,'77 Live



sp.trace = False

# find album by name
#i and j are ranges of rows in df to search for albums
i = 298
j = 300

# get the first album uri
df = df.loc[i:j]
df = df[['Artist', 'Album']]

for index, row in df.iterrows():
    #Specifies artist as well by concatinating in order to improve search accuracy of album
    albumName = str(row['Album']) + " " + str(row['Artist'])
    #print(albumName) (for testing)
    results = sp.search(q="album:" + albumName, type="album")
    album_uri = results['albums']['items'][0]['uri']
    album_title = sp.album(album_uri)
    print(str(i), str(album_title['name']))
    i+=1

# get album tracks and testing to get accurate results
'''album = 'Kid A Radiohead'
results = sp.search(q="album:" + album, type="album")
album_uri = results['albums']['items'][0]['uri']
tracks = sp.album_tracks(album_uri)
for track in tracks['items']:
    print(track['name'])

results = sp.audio_features(album_uri)
print(results)'''
