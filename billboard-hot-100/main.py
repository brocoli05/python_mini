import export
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv  # to load environment variables from .env file
import os  # to access the environment variables

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "https://example.com"
SCOPE = "playlist-modify-private"  # Write access to a user's private playlists

# Scrap Billboard 100
URL = "https://www.billboard.com/charts/hot-100/"

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(URL+year)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

songs = soup.select("li ul li h3")
songs_title = [song.getText().strip() for song in songs]
print(songs_title)

# Spotify Authentication (OAuth)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SCOPE,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        cache_path="token.txt",
        show_dialog=True,
    )
)

user_id = sp.current_user()["id"]

# Search Spotify for songs by title
song_uris = []
date = year.split("-")[0]

for title in songs_title:
    result = sp.search(q=f"track:{title} year:{date}", type="track", limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Could not find song: {title}")

# Create a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
playlist_id = (playlist["id"])

# Add songs found into the new playlist
if song_uris:
    sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
else:
    print("No songs found to add to the playlist.")