import csv
from currency import Currency

HEADER_ROW = ["Currency", "Red cup bottom Value (USDT$)", "Green cup top value (USDT$)"]


def save_currencies(currencies: list[Currency], file_name: str):
    with open(file_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(HEADER_ROW)

        for curr in currencies:
            writer.writerow(curr.get_info())

    print("saved as " + file_name)
