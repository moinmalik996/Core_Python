import json
import requests

# data = json.load(open("data.json"))
API_URL = "https://data.nasdaq.com/api/v3/datasets/BSE/BOM504991.json?api_key=TfzTyZaT-s2Q_riMgsyD"

request = requests.get(url=API_URL)
request = request.text

print(request)
print(type(request))

data = json.loads(request)
print(data)
print(type(data))

# data_serialized = json.dumps(data)
data_serialized = json.dump(data, open('data.json', 'w'), indent=5)

