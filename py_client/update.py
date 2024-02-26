import requests

endpoint = 'http://127.0.0.1:5000/api/products/2/update'

data = {
    'title': 'hello my old friend',
    
    'price' : 69
}

get_response = requests.put(endpoint, json = data )
print(get_response.status_code)
print(get_response.json())

