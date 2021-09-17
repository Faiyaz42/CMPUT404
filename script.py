import requests

print("requests version = ",requests.__version__)

print("GET requests status code = ",requests.get("http://google.com/"))

x = requests.get("https://raw.github.com/Faiyaz42/CMPUT404/main/script.py")
print(x.text)

