import requests
import json
import unittest
import pandas as pd
import sqlalchemy as db
from brawl_post import fetch_brawlers, process_brawlers, save_to_db, query_brawlers

class TestBrawlPost(unittest.TestCase):
    def test_fetch_brawlers_returns_dict(self):
        data = fetch_brawlers()

        self.assertIsInstance(data, dict)
    
    def test_process_brawlers_returns_dataframe(self):
        sample = {"items": []}
        df = process_brawlers(sample_data)

        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_save_to_db_returns_engine(self):
        df = pd.DataFrame([{"name": "Shelly", "starPowers": "[]", "gadgets": "[]"}])
        engine = save_to_db(df)

        self.assertIsInstance(engine, db.engine.Engine)
    
    def test_query_brawlers_returns_results(self):
        df = pd.DataFrame([{"name": "Shelly", "starPowers": "[]", "gadgets": "[]"}])
        engine = save_to_db(df)
        result = query_brawlers(engine)

        self.assertTrue(len(result) > 0)
        self.assertTrue(hasattr(result[0], "_mapping"))

if __name__ == '__main__':
    unittest.main()
