import requests
import json
import pandas as pd
import sqlalchemy as db



API_BASE = "https://api.brawlstars.com/v1"
HEADERS = {
  "Authorization": "Bearer "
}

def fetch_brawlers():
    response = requests.get(f"{API_BASE}/brawlers", headers=HEADERS)
    response.raise_for_status()  # Optional: helps in testing exceptions
    return response.json()

def process_brawlers(data):
    df = pd.DataFrame(data["items"])
    df['starPowers'] = df['starPowers'].apply(json.dumps)
    df['gadgets'] = df['gadgets'].apply(json.dumps)
    return df

def save_to_db(df):
    engine = db.create_engine('sqlite:///brawl_stars.db')
    df.to_sql('brawlers', con=engine, if_exists='replace', index=False)
    return engine

def query_brawlers(engine):
    with engine.connect() as connection:
        query_result = connection.execute(
            db.text("SELECT * FROM brawlers;")
        ).fetchall()
    return query_result