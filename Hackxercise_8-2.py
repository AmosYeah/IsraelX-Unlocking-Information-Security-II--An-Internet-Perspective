# Hackxercise_8-2

# Use the requests module to:

# In get, send a GET request to http://httpbin.org/status/204 and return the status code
# In post, send a POST request to http://httpbin.org/post with the data  𝑥=1  and  𝑦=2  and return the response

import requests
import json

def get():
    r = requests.get('http://httpbin.org/status/204')
    return r.status_code

def post():
    my_data = {'x': '1', 'y': '2'}
    response = requests.post('http://httpbin.org/post', data = my_data)
    return response
    
# test
print(get())
print(post())