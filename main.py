import datetime
import csv_utils
import web_utils
from currency import Currency
from threading import Thread


def main():
    def parse_currency(name, _list_):
        tmp = Currency(
            name,
            web_utils.get_bot_value(name),
            web_utils.get_top_value(name)
        )
        _list_.append(tmp)

    file_name = datetime.datetime.now().strftime("%m.%d.%Y %H-%M")
    currencies = web_utils.get_currencies()
    curr_list = []
    threads = []

    for curr in currencies:
        thread = Thread(target=parse_currency, args=(curr, curr_list,))
        threads.append(thread)

    for t in threads:
        t.start()
        t.join()

    csv_utils.save_currencies(curr_list, file_name)


if __name__ == "__main__":
    main()
