import requests

print("requests version = ",requests.__version__)

print("GET requests status code = ",requests.get("http://google.com/"))
