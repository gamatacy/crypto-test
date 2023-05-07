import json
from string import Template
import pprint
import requests
import lxml
from bs4 import BeautifulSoup as bs
from gate_io import GateIo
from ascendex import Ascendex
from mexc import Mexc
from huobi import Huobi

MEXC = Mexc()
GATE_IO = GateIo()
HUOBI = Huobi()
ASCENDEX = Ascendex()

res = requests.get(HUOBI.get_api_url("BTC","USDT"))
soup = bs(res.text, "lxml")
load = json.loads(soup.text)

# Idk how it works
# UNISWAP = Market("UNISWAP", Template("https://api.uniswap.org/v1/quote?protocols=v2%2Cv3%2Cmixed&"
#                                      "tokenInAddress= $main &tokenInChainId=1&"
#                                      "tokenOutAddress= $second "
#                                      "&tokenOutChainId=1&amount=1000000&type=exactIn"))


