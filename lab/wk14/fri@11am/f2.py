import requests

site_url = "https://YOUR.gblearn.com"
response = requests.get(site_url, auth=("username", "passsword"))














print(response.text)

with open("mygblearn.html", mode="w", encoding="utf-8") as file:
    file.write(response.text)
