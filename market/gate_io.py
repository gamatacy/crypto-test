from string import Template
from market.market import Market


class GateIo(Market):

    def __init__(self, name="GateIo", url=Template("https://api.gateio.ws/api/v4/spot/order_book?currency_pair=$main "
                                                   "_ $second"), upper_case=True):
        super().__init__(name, url, upper_case)

    def get_prices(self, load):
        try:
            return {"asks": load["asks"], "bids": load["bids"]}
        except:
            return {"asks": "unavailable", "bids": "unavailable"}
