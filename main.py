import datetime
import csv_utils
import web_utils
from currency import Currency


def main():
    currencies = web_utils.get_currencies()
    curr_list = []

    for curr in currencies:
        tmp = Currency(
            curr,
            web_utils.get_bot_value(curr),
            web_utils.get_top_value(curr)
        )

        curr_list.append(tmp)

    csv_utils.save_currencies(curr_list, datetime.datetime.now().strftime("%m.%d.%Y %H-%M"))


if __name__ == "__main__":
    main()
