import requests
# from products.models import Product
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = 'http://127.0.0.1:8000/api/'

# pro = Product.objects.get(id=1)
get_response = requests.post(endpoint, params={'abc': 123}, json = {'title':"helloh world"})
print(get_response.status_code)
print(get_response.json())

# {
#   "args": {}, 
#   "data": "", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.30.0", 
#     "X-Amzn-Trace-Id": "Root=1-64568653-7a81f6c831621ac260164190"
#   }, 
#   "json": null, 
#   "method": "GET", 
#   "origin": "2.123.129.172", 
#   "url": "https://httpbin.org/anything"
# }

# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.30.0', 'X-Amzn-Trace-Id': 'Root=1-64568724-4ad8de623efecee0187d10da'}, 'json': None, 'method': 'GET', 'origin': '2.123.129.172', 'url': 'https://httpbin.org/anything'}
