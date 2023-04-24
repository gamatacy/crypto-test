import json
import requests
import lxml
from bs4 import BeautifulSoup as bs

CRYPTO_TOP_URL = "https://coinmarketcap.com/"
TEST_CRYPTO_TOP_URL = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=11&limit=140&sortBy" \
                      "=market_cap&sortType=desc&convert=USD,BTC," \
                      "ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs," \
                      "cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d," \
                      "self_reported_circulating_supply,self_reported_market_cap"
RED_CUP_URL = "https://ascendex.com/api/pro/v1/depth?symbol="
GREEN_CUP_URL = "https://api.gateio.ws/api/v4/spot/order_book?currency_pair="
SECOND_CURRENCY = "USDT"


def get_currencies():
    currencies = []

    res = requests.get(TEST_CRYPTO_TOP_URL)
    soup = bs(res.text, "lxml")
    load = json.loads(soup.text)

    for symbol in load["data"]["cryptoCurrencyList"]:
        currencies.append(symbol["symbol"])

    return currencies


def get_bot_value(curr: str):
    res = requests.get(RED_CUP_URL + curr.upper() + "/" + SECOND_CURRENCY)

    try:
        soup = bs(res.text, "lxml")
        load = json.loads(soup.text)
        return '{0:.7f}'.format(float(load["data"]["data"]["asks"][0][0]))
    except:
        print("Rate limit")
        return "unavailable"


def get_top_value(curr: str):
    res = requests.get(GREEN_CUP_URL + curr.upper() + "_" + SECOND_CURRENCY)

    try:
        soup = bs(res.text, "lxml")
        load = json.loads(soup.text)
        return '{0:.7f}'.format(float(load['bids'][0][0]))
    except:
        return "unavailable"
