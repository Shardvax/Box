import requests

http_endpoint = "https://api.nasa.gov/planetary/apod?api_key=w5bmNFQ66DXoN115ladQRzmbIQeFuce2pvrdRvN5"
http_parameters = {
	"date": "2004-11-21"
}
req = requests.get(http_endpoint, params=http_parameters)
result = req.json()
print(result)