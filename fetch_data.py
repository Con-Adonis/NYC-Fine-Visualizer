import duckdb
import requests

url = "https://data.cityofnewyork.us/resource/jz4z-kudi.json"
params = {"$limit": 50000, "$$app_token": "jQ5Aq1Bt4SKDx7YXZlATs0Iqa"}

data = requests.get(url, params=params).json()

print(data)