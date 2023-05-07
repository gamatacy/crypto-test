from string import Template

from market.market import Market


class Ascendex(Market):

    def __init__(self, name="Ascendex", url=Template("https://ascendex.com/api/pro/v1/depth?symbol=$main / $second"),
                 upper_case=True):
        super().__init__(name, url, upper_case)

    def get_prices(self, load):
        try:
            return {"asks": load["data"]["data"]["asks"], "bids": load["data"]["data"]["bids"]}
        except:
            return {"asks": "unavailable", "bids": "unavailable"}
