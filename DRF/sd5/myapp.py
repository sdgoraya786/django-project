# 3
import requests
import json

URL = "http://127.0.0.1:8000/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url = URL, data = json_data )
    stu_data = res.json()
    print(stu_data)

# get_data()

def post_data():
    data = {
        'name' : 'Sadnan',
        'roll' : 13,
        'city' : 'Faqeerwali'
    }
    json_data = json.dumps(data)
    res = requests.post(url = URL, data = json_data )
    insert_res = res.json()
    print(insert_res)
    get_data()
post_data()

def update_data():
    data = {
        'id' : 8,
        'name' : 'SD Goraya'
    }
    json_data = json.dumps(data)
    res = requests.put(url = URL, data = json_data )
    insert_res = res.json()
    print(insert_res)
    get_data(8)
# update_data()

def delete_data():
    data = {
        'id' : 7
    }
    json_data = json.dumps(data)
    res = requests.delete(url = URL, data = json_data )
    insert_res = res.json()
    print(insert_res)
    get_data()
# delete_data()