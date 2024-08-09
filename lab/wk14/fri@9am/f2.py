import requests

site_url = "https://www.georgebrown.ca/"

result = requests.request("get", site_url)
print(result.text)

