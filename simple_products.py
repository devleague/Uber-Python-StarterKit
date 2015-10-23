import os
import requests
import json

url = 'https://sandbox-api.uber.com/v1/products'

parameters = {
  'server_token': os.environ['UBER_SERVER_TOKEN'],
  'latitude': 21.3088619,
  'longitude': -157.8086674
}

response = requests.get(url, params=parameters)

data = json.dumps( response.json(), indent=2 )

print(data)
