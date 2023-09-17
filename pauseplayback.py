import spotipy
import sys
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

scope = 'user-read-playback-state user-modify-playback-state'

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= "4d502f92f4834f4483913b53415b4e24", client_secret= "4b050805c79940aeb6fc5d84eab88ba2", redirect_uri= "https://localhost:8888/callback", scope = "user-read-playback-state user-modify-playback-state"))

#spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

sp.pause_playback()
'''
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()
'''
