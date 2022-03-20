import requests

endpoint = "http://localhost:8000/api/products/1/" # http://127.0.0.1:8000/

get_response = requests.get(endpoint) # Application Programming Interface -> REST API (HTTP Requests)

print (get_response.json())