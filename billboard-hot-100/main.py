import export
from bs4 import BeautifulSoup
import requests
import spotipy

URL = "https://www.billboard.com/charts/hot-100/"

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(URL+year)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

songs = soup.select("li ul li h3")
songs_title = [song.getText().strip() for song in songs]
print(songs_title)
