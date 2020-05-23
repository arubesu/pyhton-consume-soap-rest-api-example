import requests
import json

result = requests.get('https://api.github.com/users/arubesu/repos?page=1&per_page=20')
raw = result.json()

for index in raw:
  print(index['name'])


