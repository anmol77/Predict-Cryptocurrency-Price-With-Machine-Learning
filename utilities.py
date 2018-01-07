from datetime import datetime, timedelta
import pandas as pd # data processing, CSV file I/O
import urllib.request
import json
import os


bitcoin_start_date = "2013-09-01"


def get_date_from_current():
    return datetime.now().date() - timedelta(days=offset)


def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")


def fetch_historical_bitcoin_data_to_date():
    stop_date = get_date_from_current(offset=0)
    url = ("https://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s" % (bitcoin_start_date, stop_date))
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, None, headers)

    create_data_folder()
    currency_file_path = 'data/BTC_%s_%s.csv' % (bitcoin_start_date, stop_date)

    if not os.path.exists(currency_file_path):
        with urllib.request.urlopen(request) as url:
            data = json.loads(url.read().decode())
            with open(currency_file_path, 'w') as price_file:
                price_file.write("date,close\n")
                for date in data['bpi']:
                    price_file.write("%s,%s\n" % (date, data['bpi'][date]))


def get_dataset(currency="BTC"):
    if currency == "BTC":
        return pd.read_csv('data/BTC_%s_%s.csv' % (bitcoin_start_date,
                                                   get_date_from_current(offset=0)),
                           header=0)
