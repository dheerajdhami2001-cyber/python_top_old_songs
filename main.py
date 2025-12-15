from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="ddc8977b4c6c49d780ff695effc86cf5",
        client_secret="8dc36fa7766c479b8e78892f1600afc2",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token_new.txt"
    )
)

print(sp.current_user()["id"])

date = input("which time you want to travel ? YYYY-MM-DD:")
response =  requests.get(f"https://kworb.net/ww/archive/{date}.html")
songs = response.text

soup = BeautifulSoup(songs, "html.parser")
top_songs = soup.find_all("td",class_="mp text")

top = []
top_uri = []

for song in top_songs:
    top.append(song.text.split("-")[1])

for tracks in top[:11]:
    try:
        track_uri = sp.search(q = f"track:{tracks} year:{date[:4]}",type = "track")
        uri = track_uri["tracks"]["items"][0]["uri"]
        top_uri.append(uri)

    except IndexError:
        print(f"{tracks} not found")

print(top_uri)

playlist = sp.user_playlist_create(user="31fls3vbkfmr2dqafus2d46hczyi",name=f"gold of {date[:4]}-{date[4:6]}-{date[6:]}",public=False)
print(playlist["id"])
sp.playlist_add_items(playlist_id = playlist["id"],items= top_uri)
print(f"your playlist of {len(top_uri)} is now created")