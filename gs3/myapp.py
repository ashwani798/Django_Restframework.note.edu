import requests
import json

url = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}
    
    r = requests.get(url=url, params=params, headers={'Content-Type': 'application/json'})
    data = r.json()
    print('GET Response:', data)

def post_data():
    data = {
        'name': 'jason',
        'roll': 4,
        'city': 'kota'
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data, headers={'Content-Type': 'application/json'})
    data = r.json()
    print('POST Response:', data)

def update_data():
    data = {
        'id': 4,
        'name': 'Trudo',
        'city': 'Agra'
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data, headers={'Content-Type': 'application/json'})
    data = r.json()
    print('PUT Response:', data)

# Uncomment to call the function you want to test
# get_data(1)
# post_data()
update_data()


def delete_data():
    data = {'id': 3}
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)

delete_data()
