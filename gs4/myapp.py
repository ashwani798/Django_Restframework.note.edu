import requests
import json

url = 'http://127.0.0.1:8000/studentapi/'


def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}
    
    r = requests.get(url=url, params=params)  # Use params for query parameters
    data = r.json()
    print(data)

# Uncomment to test get_data function
#get_data()

def post_data():
    data = {
        'name': 'gio',
        'roll': 5,
        'city': 'kerla',
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, json=data)  # Use json to send JSON data
    data = r.json()
    print(data)

# Uncomment to test post_data function
post_data()

def update_data():
    data = {
        'id': 5,
        'name': 'Trudo',
        'city': 'Agra'
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, json=data)  # Use json to send JSON data
    data = r.json()
    print(data)

# Uncomment to test update_data function
#update_data()

def delete_data():
    data = {'id': 3}
    json_data = json.dumps(data)
    r = requests.delete(url=url, json=data)  # Use json to send JSON data
    data = r.json()
    print(data)

# Uncomment to test delete_data function
#delete_data()
