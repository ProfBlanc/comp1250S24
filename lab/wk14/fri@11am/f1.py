#
import requests
import re
site_url = "https://www.georgebrown.ca"
response = requests.get(site_url)

# print(response.text)

images = response.text.count("<img")
print(images)

images = re.findall(r"<img.+/>", response.text)

for image in images:
    print(image)
