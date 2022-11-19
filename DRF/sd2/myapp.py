# Seprate application
# This file not a part of sd1
import requests
import json

URL = "http://127.0.0.1:8000/"

data = {
    'name' : 'Adnan',
    'roll' : 4,
    'city' : 'Lahore'
}

json_data = json.dumps(data)
r = requests.post(url = URL, data=json_data)
d = r.json()
print(d)
