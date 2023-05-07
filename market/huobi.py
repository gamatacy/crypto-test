from string import Template
from market.market import Market


class Huobi(Market):

    def __init__(self, name="HUOBI",
                 url=Template("https://api.huobi.pro/market/depth?symbol=$main $second &type=step0"), upper_case=False):
        super().__init__(name, url, upper_case)

    def get_prices(self, load):
        try:
            return {"asks": load["tick"]["asks"], "bids": load["tick"]["bids"]}
        except:
            return {"asks": "unavailable", "bids": "unavailable"}