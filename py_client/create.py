import requests

endpoint = "http://localhost:8000/api/products/" # http://127.0.0.1:8000/

data = {
    "title": "This field is done",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data) # Application Programming Interface -> REST API (HTTP Requests)

print (get_response.json())