import duckdb
import pandas as pd
import requests

url = "https://data.cityofnewyork.us/resource/jz4z-kudi.json"
params = {"$limit": 3, "$$app_token": "Inxt007JrEdJQwKaX5XcYkfFC"}

data = requests.get(url, params=params).json()
df = pd.DataFrame(data)

db = duckdb.connect("data.duckdb")
duckdb.register(db, "data", df)
db.execute("CREATE TABLE IF NOT EXISTS oath AS SELECT * FROM data")
db.table("oath").show()
db.close()

# the data was able to be turned into a pandas dataframe (can be read by duck db)
# all thats needed now is to understand how to connect to data.duckdb, write the info to it, and query (docs in firefox tab)