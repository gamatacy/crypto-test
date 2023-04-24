import datetime
from time import sleep

import csv_utils
import web_utils
from currency import Currency
from threading import Thread

currencies = ['1INCH',
              'LRC',
              'ZEC',
              'BSV',
              'INJ',
              'CRV',
              'CHZ',
              'SAND',
              'AXS',
              'XTZ',
              'EGLD',
              'WOO']

curr_list = currencies.copy()


def parse_currency(name):
    tmp = Currency(
        name,
        web_utils.get_bot_value(name),
        web_utils.get_top_value(name)
    )

    curr_list[currencies.index(tmp.name)] = tmp


def main():
    global curr_list

    threads = []

    for i in range(5000):
        print(i)
        file_name = datetime.datetime.now().strftime("%m.%d.%Y %H-%M-%S")
        for curr in currencies:
            thread = Thread(target=parse_currency, args=(curr,))
            threads.append(thread)
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        csv_utils.save_currencies(curr_list, "results/" + file_name)
        threads.clear()
        curr_list = currencies.copy()
        sleep(6)


if __name__ == "__main__":
    main()
