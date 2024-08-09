import requests
from bs4 import BeautifulSoup

site_url = "https://www.georgebrown.ca"
response = requests.get(site_url)

soup = BeautifulSoup(response.text, "html.parser")

all_links = soup.find_all("a")
print("Number of links = ", len(all_links))
# for link in all_links:
#     print(link)

print(soup.title.string)

print(all_links[0].name)  # name of the tag: 'a'

print(all_links[0].attrs["href"])
print(all_links[0])

all_links[0].attrs["href"] = "I love python"
print(all_links[0].attrs["href"])
print(all_links[0])
