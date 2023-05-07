from string import Template
from market.market import Market


class Mexc(Market):

    def __init__(self, name="MEXC", url=Template("https://futures.mexc.com/api/v1/contract/depth_step/$main _ $second"),
                 upper_case=True):
        super().__init__(name, url, upper_case)

    def get_prices(self, load):
        try:
            return {"asks": load["data"]["asks"], "bids": load["data"]["bids"]}
        except:
            return {"asks": "unavailable", "bids": "unavailable"}
