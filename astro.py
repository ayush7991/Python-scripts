import requests
import json

req = requests.get('http://api.open-notify.org/astros.json')
r=req.json()
re=r['people']
for data in re:
    print('---------------')
    print(data['name'])
