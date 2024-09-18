import requests

url = 'http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}
    
    r = requests.get(url=url, params=params)
    
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:", r.text)

# Uncomment to test get_data function
get_data()

def post_data():
    data = {
        'name': 'gio',
        'roll': 5,
        'city': 'kerla',
    }
    
    r = requests.post(url=url, json=data)
    
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:", r.text)

# Uncomment to test post_data function
# post_data()

def update_data():
    data = {
        'id': 5,
        'name': 'Trudo',
        'city': 'Agra'
    }
    
    r = requests.put(url=url, json=data)
    
    try:
        data = r.json()
        print(data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:", r.text)

# Uncomment to test update_data function
# update_data()

def delete_data():
    data = {'id': 3}
    
    r = requests.delete(url=url, json=data)
    
    try:
        # delete requests typically don't return JSON data,
        # but some APIs may return a success message or an empty response
        if r.status_code == 204:
            print("Delete successful, no content returned.")
        else:
            data = r.json()
            print(data)
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response was:", r.text)

# Uncomment to test delete_data function
# delete_data()
