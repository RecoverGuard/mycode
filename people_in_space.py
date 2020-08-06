#!/usr/bin/env
import requests
import json


url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

astros= response.json()
print(astros)

print(f"People in space: ", astros['number'])

for x in astros['people']:
    print(x['name'] + ' is on the ' + x['craft'])
