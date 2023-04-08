import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver

CRYPTO_TOP_URL = "https://coinmarketcap.com/"
RED_CUP_URL = "https://ascendex.com/ru/cashtrade-spottrading/usd/"
GREEN_CUP_URL = "https://www.gate.io/ru/trade/"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.headless = True


def get_currencies():
    currencies = []

    res = requests.get(CRYPTO_TOP_URL)
    soup = bs(res.text, "html.parser")
    top_10 = soup.find_all('p', class_="coin-item-symbol")

    for pos in top_10:
        currencies.append(pos.text)

    return currencies


def get_bot_value(currency):
    url = RED_CUP_URL + currency.lower()

    driver.get(url)
    res = driver.page_source
    soup = bs(res, "html.parser")
    value = soup.find('span', class_="span-body price down-color")

    return float(value.text)


def get_top_value(currency):
    url = GREEN_CUP_URL + currency.upper() + "_USD"

    driver.get(url)
    res = driver.page_source
    soup = bs(res, "html.parser")
    value = soup.find('span', class_="price font-add-color")

    return float(value.text)
