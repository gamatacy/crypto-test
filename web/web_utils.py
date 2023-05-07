import json
import requests
import lxml
from bs4 import BeautifulSoup as bs

from currency.currency import Currency
from market.ascendex import Ascendex
from market.gate_io import GateIo
from market.huobi import Huobi
from market.mexc import Mexc


def init_markets():
    return [Mexc(), GateIo(), Huobi(), Ascendex()]


def parse_currency(main_currency, second_currency, currs):
    markets = init_markets()

    prices = {}

    for market in markets:
        try:
            url = market.get_api_url(main_currency, second_currency)
            res = requests.get(url)
            soup = bs(res.text, "lxml")
            load = json.loads(soup.text)
            price = market.get_prices(load)
            prices[market.name] = price
        except:
            price = market.get_prices('')
            prices[market.name] = price

    currency = Currency(main_currency, prices)

    currs.append(currency)
