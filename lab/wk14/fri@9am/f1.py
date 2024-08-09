from urllib.request import urlopen

import re
site_url = "https://www.georgebrown.ca/"

page = urlopen(site_url)
# print(page)
# print(page.read().decode())

match = re.search("<img.+/>", page.read().decode())
if match:
    print(match.group())

page.close()
