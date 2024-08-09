import requests
from bs4 import BeautifulSoup

site_url = "https://www.georgebrown.ca/"

html = requests.request("GET", site_url).text

soup = BeautifulSoup(html, "html.parser")
num_links = len(soup.find_all("a"))
num_images = len(soup.find_all("img"))

print("There are", num_links, "links and", num_images, "images",
      "on the website", soup.title.string, "at url", site_url)
