import requests
from bs4 import BeautifulSoup

site_url = "https://www.georgebrown.ca/"

html = requests.request("GET", site_url).text

soup = BeautifulSoup(html, "html.parser")
# print(soup)
open("georgebrown1.html", mode="w", encoding="utf-8").write(str(soup))
