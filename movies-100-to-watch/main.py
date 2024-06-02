import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

titles = soup.find_all(name="h3", class_="title")
# get all movie titles without html tags
title_texts = [title.getText() for title in titles]
title_texts.reverse()  # movie_texts[::-1]
print(title_texts)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in title_texts:
        file.write(f"{title}\n")
