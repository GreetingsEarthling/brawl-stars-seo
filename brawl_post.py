import requests
import json
import pandas as pd
import sqlalchemy as db

API_BASE = "https://api.brawlstars.com/v1"
HEADERS = {
  "Authorization": "Bearer "
}

response = requests.get(f"{API_BASE}/brawlers", headers=HEADERS)
data = response.json()

df = pd.DataFrame(data["items"])
df['starPowers'] = df['starPowers'].apply(json.dumps)
df['gadgets'] = df['gadgets'].apply(json.dumps)

engine = db.create_engine('sqlite:///brawl_stars.db')
df.to_sql('brawlers', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
  query_result = connection.execute(db.text("SELECT * FROM brawlers;")).fetchall()

print(pd.DataFrame(query_result))