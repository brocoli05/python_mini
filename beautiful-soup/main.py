from bs4 import BeautifulSoup
import lxml
import requests

# requests: allows to get hold of the data from a particular URL
response = requests.get("https://news.ycombinator.com/")
# print(response.text)

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

# TODO: Store the title of the first article under article_text using BeautifulSoup.
# TODO: Then print the title to the PyCharm Console
article_tag = soup.find(name="span", class_="titleline")
article_text = article_tag.a.getText()
article_link = article_tag.a.get("href")
article_upvote = soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.a.getText()
    article_link = article_tag.a.get("href")
    article_texts.append(article_text)
    article_links.append(article_link)

# article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)
# get only number
# print(int(article_upvotes[0].split()[0]))

# TODO: Print out the title and link for the story with the highest number of upvotes.
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])


# for article in article_text:
#     print(article.getText())

# # TODO: Open the website.html.
# # TODO: Store all of its text in a variable called contents.
# # UnicodeDecodeError ==> encoding="utf-8"
# with open(file="website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "lxml")  # "html.parser"
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.a)
# print(soup.p)

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.name)
# print(section_heading.get("class"))
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# company_name = soup.select_one(selector="#name")
# print(company_name)
#
# headings = soup.select(".heading")
# print(headings)
