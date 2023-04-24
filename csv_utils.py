import csv
import os
from currency import Currency

HEADER_ROW = ["Currency", "AscendEX bottom Value (USDT$)", "GateIO top value (USDT$)", "Difference"]


def save_currencies(currencies: list[Currency], file_name: str):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(HEADER_ROW)

        for curr in currencies:
            writer.writerow(curr.get_info())

    print("saved as " + file_name)
