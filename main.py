import datetime
from time import sleep

import csv_utils
import web_utils
from currency import Currency
from threading import Thread


def parse_currency(name, curr_list):
    tmp = Currency(
        name,
        web_utils.get_bot_value(name),
        web_utils.get_top_value(name)
    )

    curr_list[curr_list.index(tmp.name)] = tmp


def main():
    file_name = datetime.datetime.now().strftime("%m.%d.%Y %H-%M-%S")
    currencies = web_utils.get_currencies()
    threads = []

    for curr in currencies:
        thread = Thread(target=parse_currency, args=(curr, currencies,))
        threads.append(thread)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    csv_utils.save_currencies(currencies, file_name)


if __name__ == "__main__":
    main()
