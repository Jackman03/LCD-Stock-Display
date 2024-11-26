#It's older code, but it checks out
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def GetCurrentPrice(Ticker):
    url = 'https://finance.yahoo.com/quote/' + Ticker +'/'

    r = requests.get(url)

    if r.status_code == 200:
        texts = BeautifulSoup(r.text,'html.parser')

        try:
            price = texts.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
            change = texts.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text
            return price, change
        except AttributeError:
            return -2

    #404 error indicates page not found. So in our case it would likely be invalid ticker 
    elif r.status_code == 404:
        return -1
    else:
        return -3, r.status_code
