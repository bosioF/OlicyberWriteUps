import requests

url = 'http://web-10.challs.olicyber.it/'
header = {'Unauthorized': 'Authorized'}

request_option = requests.options(url)
if 'Allow' in request_option.headers:
    allowed_methods = request_option.headers['Allow']
    print(allowed_methods)

r = requests.patch(url, headers=header)
print(r.headers)





