import requests
from bs4 import BeautifulSoup

site_url = "https://www.georgebrown.ca/"

html = requests.request("GET", site_url).text

soup = BeautifulSoup(html)
print(soup.prettify())

images = soup.find_all("img")

for image in images:
    print(image)

print("*" * 20)
links = soup.find_all("a")
for link in links:
    print(link)
print("*" * 20)
print(images[0])
print(images[0].attrs['src'])
print(images[0].attrs['alt'])
