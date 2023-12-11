import spotipy
from spotipy.oauth2 import SpotifyOAuth
from savify import Savify
from savify.utils import PathHolder

scope = "user-follow-read," \
        "user-library-read," \
        "user-library-modify," \
        "user-modify-playback-state," \
        "user-read-playback-state," \
        "user-read-currently-playing," \
        "app-remote-control," \
        "playlist-read-private," \
        "playlist-read-collaborative," \
        "playlist-modify-public," \
        "playlist-modify-private," \
        "streaming"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

urls = []
results = sp.current_user_playlists(limit=50)

while(results):
    playlists = results['items']
    for playlist in playlists:
        urls.append(playlist['external_urls']['spotify'])
        print(playlist['name'])
    results = results['next']

s=Savify(path_holder=PathHolder(downloads_path='/Users/toothless/Desktop/songs'), group='%playlist%')

s.download('https://open.spotify.com/playlist/6blWHoeSWJ8N97O1LCA9FN?si=0fd5505f55044ce9')
for url in urls:
    s.download(url)
print(urls)
#     for _, item in enumerate(results['items']):
#         track = item['track']
#         tracks.append(UserTrack(track['name'], track['artists'][0]['name'], track['album']['name'], track['uri']))
#     results = sp.next(results)
# for _, item in enumerate(results['items']):
#     track = item['track']
#     tracks.append(UserTrack(track['name'], track['artists'][0]['name'], track['album']['name'], track['uri']))
# return tracks