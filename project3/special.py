### for privacy my own user information has been omitted, but in special.png I've used my own information as demonstration. ### 
## try it yourself! ## 

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt
from collections import Counter
import time

# replace id and secret with your own from spotify 
client_id = 'your_client_id'
client_secret = 'your_client_secret'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# get user data
user_id = 'your_user_id'

top_tracks = sp.current_user_top_tracks(limit=50, time_range='short_term')


# get user's top genres from artist information
genres = []
for track in top_tracks['items']:
    track_info = sp.track(track['id'])
    for artist in track_info['artists']:
        artist_info = sp.artist(artist['id'])
        if 'genres' in artist_info:
            artist_genres = artist_info['genres']
            genres.extend(artist_genres)

genre_counts = Counter(genres)

# make visualization
plt.figure(figsize=(10, 6))
plt.bar(genre_counts.keys(), genre_counts.values())
plt.xlabel('Genres')
plt.ylabel('Number of Tracks')
plt.title('Top Music Genres on Spotify')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()
