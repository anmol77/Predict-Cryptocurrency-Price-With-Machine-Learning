from datetime import datetime, timedelta
import pandas as pd # data processing, CSV file I/O
import urllib.request
import json
import os


bitcoin_start_date = "2013-09-01"


def get_date_from_current(offset):
    return datetime.now().date() - timedelta(days=offset)


def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")


def get_dataset(currency="BTC"):
    folder_path = "CryptoAI-CoinMarketCapHistoricalDataScraper/data/%s.csv" % currency
    return pd.read_csv(folder_path, header=0)
