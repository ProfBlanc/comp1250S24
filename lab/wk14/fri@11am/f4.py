import requests
from bs4 import BeautifulSoup

site_url = "https://www.georgebrown.ca"
response = requests.get(site_url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all("a")
styles = soup.find_all("link")
images = soup.find_all("img")

for image in images:

    if "src" in image.attrs and  image.attrs["src"].startswith("/"):
        image.attrs["src"] = site_url + image.attrs["src"]


for link in links:
    if link.attrs["href"].startswith("/"):
        link.attrs["href"] = site_url + link.attrs["href"]

for style in styles:
    if style.attrs["href"].startswith("/"):
        style.attrs["href"] = site_url + style.attrs["href"]


open("georgebrown.html", mode="w", encoding="utf-8").write(str(soup))
