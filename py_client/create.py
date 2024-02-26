import requests
from getpass import getpass


auth_endpoint = 'http://127.0.0.1:4000/api/auth/'
password = getpass()
auth_response = requests.post(auth_endpoint, json = {'username' : 'staff', 'password':password})
print(auth_response.json())




endpoint = 'http://127.0.0.1:4000/api/products/'
try:
    csrf_token = requests.post(endpoint).cookies['csrftoken']
except:
    print('some issue')

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization' : f'Token {token}',
        'X-CSRFToken' : csrf_token
    }
    data = {
        'title' : 'put in whateva'
    }
    
    get_response = requests.get(endpoint, json = data, headers=headers)
    print(get_response.status_code)
    print(get_response.json())

