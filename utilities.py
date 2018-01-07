from datetime import datetime
import urllib.request
import json
import os


def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")


def fetch_historical_bitcoin_data_to_date():
    start_date = "2013-09-01"
    stop_date = datetime.now().date()
    url = ("https://api.coindesk.com/v1/bpi/historical/close.json?start=%s&end=%s" % (start_date, stop_date))
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, None, headers)

    create_data_folder()

    with urllib.request.urlopen(request) as url:
        data = json.loads(url.read().decode())
        with open('data/BTC_%s_%s' % (start_date, stop_date), 'w') as price_file:
            for date in data['bpi']:
                price_file.write("%s, %s\n" % (date, data['bpi'][date]))
