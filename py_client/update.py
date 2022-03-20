import requests

endpoint = "http://localhost:8000/api/products/1/update/" # http://127.0.0.1:8000/

data = {
    "title": "Hello world my old friend",
    "price": 129.99
}

get_response = requests.put(endpoint, json=data) # Application Programming Interface -> REST API (HTTP Requests)

print (get_response.json())