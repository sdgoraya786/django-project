# 3
import requests
import json

URL = "http://127.0.0.1:8000/"
headers = {'content-type':'application/json'}

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url = URL, headers=headers, data = json_data )
    stu_data = res.json()
    print(stu_data)

# get_data(4)

def post_data():
    data = {
        'name' : 'Sadnan',
        'roll' : 13,
        'city' : 'Lahore'
    }
    json_data = json.dumps(data)
    res = requests.post(url = URL, headers=headers, data = json_data )
    insert_res = res.json()
    print(insert_res)
    get_data()
# post_data()

def update_data():
    data = {
        'id' : 12,
        'name' : 'Shahzad Ashraf'
    }
    json_data = json.dumps(data)
    res = requests.put(url = URL, headers=headers, data = json_data )
    insert_res = res.json()
    print(insert_res)
    get_data()
# update_data()

def delete_data():
    data = {
        'id' : 11
    }
    json_data = json.dumps(data)
    res = requests.delete(url = URL, headers=headers, data = json_data )
    insert_res = res.json()
    print(insert_res)
    get_data()
delete_data()