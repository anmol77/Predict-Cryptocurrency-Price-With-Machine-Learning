from datetime import datetime
import urllib.request
import json
import os


def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")


def fetch_historical_data():
    current_date = datetime.now().date()
    url = ("https://api.coindesk.com/v1/bpi/historical/close.json?start=2013-09-01&end=%s" % current_date)
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, None, headers)

    create_data_folder()

    with urllib.request.urlopen(request) as url:
        data = json.loads(url.read().decode())
        with open('data/%s' % current_date, 'w') as price_file:
            for date in data['bpi']:
                price_file.write("%s, %s\n" % (date, data['bpi'][date]))
