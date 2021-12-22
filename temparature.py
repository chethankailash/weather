import requests
import url
import sys

if len(sys.argv) > 2:
    print("Invalid number of Arguments, (takes only one argument city name)")
    exit(1)
if len(sys.argv) == 2:
    city=sys.argv[1]
else:
    city="current"

res = requests.get(url.URL(city))
print(res.json())
print(len(sys.argv))