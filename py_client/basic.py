import requests

endpoint = "http://localhost:8000/api/" # http://127.0.0.1:8000/

get_response = requests.post(endpoint, json={"content": "Hello World"}) # Application Programming Interface -> REST API (HTTP Requests)
# print(get_response.text) # Print raw text response
# print(get_response.status_code)


# HTTP Request
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict
print (get_response.json())