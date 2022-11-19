# Seprate application
# This file not a part of sd1
import requests

URL = "http://127.0.0.1:8000/"

r = requests.get(url = URL)
data = r.json()
print(data)
