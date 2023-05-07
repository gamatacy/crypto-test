import datetime
import pprint
from time import sleep

from utils import csv_utils
from web import web_utils
from currency.currency import Currency
from threading import Thread
import currency.static as static


currencies = []
threads = []
second_curr = "usdt"


def main():
    file_name = datetime.datetime.now().strftime("%m.%d.%Y %H-%M-%S")
    for curr in static.currencies:
        threads.append(Thread(target=web_utils.parse_currency, args=(curr, second_curr, currencies, )))
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    csv_utils.save_currencies(currencies,"results/" + file_name)



if __name__ == "__main__":
    main()
