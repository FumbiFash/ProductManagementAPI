import requests
from getpass import getpass

print('s')
auth_endpoint = 'http://127.0.0.1:4000/api/auth/'

print('f')
password = getpass()
auth_response = requests.post(auth_endpoint, json = {'username' : 'staff', 'password':password})
print(auth_response.json())

 
endpoint = 'http://127.0.0.1:4000/api/products/2'

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization' : f'Token {token}'
    }
    get_response = requests.get(endpoint)
    print(get_response.status_code)
    print(get_response.json())
  
 