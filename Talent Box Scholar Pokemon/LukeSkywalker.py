import requests

http_endpoint = "http://swapi.dev/api/people/?search="
http_parameters = {}

pick = input("Enter Who You Want To Learn About!")
http_endpoint = http_endpoint + pick

req = requests.get(http_endpoint, params=http_parameters)
result = req.json()
print(result)