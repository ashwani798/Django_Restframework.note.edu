import requests
import json  # Don't forget to import json

URL = "http://127.0.0.1:8000/stucreate/"


data = {
    'name': 'Andrew',
    'roll': 101,
    'city': 'Gonda'
}

# Use the json parameter to send JSON data
r = requests.post(url=URL, json=data)

# Get the response in JSON format
response_data = r.json()

# Print the response
print(response_data)
