import pprint


def get_diff_str(m1, m2, diff):
    return f"Ask:{m1}/Bid:{m2}: {str(diff)[:5]}%"


class Currency:

    def __init__(self, name, markets: {}):
        self.name = name
        self.markets = markets

    def get_info(self):
        return [self.name, self.markets]

    def get_diff(self):

        used = []
        diffs = []

        #pprint.pprint(self.markets)

        for market in self.markets:
            used.append(market)
            for market2 in self.markets:
                if market2 != market and market2 not in used:
                    try:

                        diff1 = float(self.markets[market]["asks"][0][0]) - float(self.markets[market2]["bids"][0][0])
                        diff2 = float(self.markets[market2]["asks"][0][0]) - float(self.markets[market]["bids"][0][0])

                        if diff1 > diff2:
                            diff = self.diff(market, market2)
                            diff_str = get_diff_str(market, market2, diff)

                        else:
                            diff = self.diff(market2, market)
                            diff_str = get_diff_str(market2, market, diff)

                        diffs.append(diff_str)

                    except:
                        diff_str = f"{market}/{market2}: unavailable"
                        diffs.append(diff_str)
                        pass

        return diffs

    def diff(self, m1, m2):
        return abs(
            (float(self.markets[m1]["asks"][0][0]) - float(
                self.markets[m2]["bids"][0][0])) / float(
                self.markets[m2]["bids"][0][0])) * 100
