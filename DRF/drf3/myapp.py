import requests
import json
from django.views.decorators.csrf import csrf_exempt

URL = "http://127.0.0.1:8000/studentapi/"


@csrf_exempt
def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {
        'content-type': 'application/json'
    }
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


@csrf_exempt
def post_data():
    data = {
        'name': 'Abbas',
        'roll': 104,
        'city': 'Karachi'
    }
    headers = {
        'content-type': 'application/json'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


@csrf_exempt
def update_data():
    data = {
        'id': 1,
        'name': 'Abbas',
        'roll': 104,
        'city': 'Karachi'
    }
    headers = {
        'content-type': 'application/json'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


def delete_data():
    data = {'id': 4}
    headers = {'content-type': 'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data()
# post_data()
# update_data()
delete_data()
