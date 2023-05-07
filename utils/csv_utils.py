import csv
import os
from currency.currency import Currency


def save_currencies(currencies: list[Currency], file_name: str):
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        header_row = ["Currency"]
        for n in currencies[0].markets:
            header_row.append(f"Asks {n}")
            header_row.append(f"Bids {n}")

        writer.writerow(header_row)

        for curr in currencies:
            row = [curr.name]
            for m in curr.markets:
                try:
                    row.append(curr.markets[m]["asks"][0][0])
                    row.append(curr.markets[m]["bids"][0][0])
                except:
                    row.append("unavailable")
                    row.append("unavailable")
            for m in curr.get_diff():
                row.append(m)
            writer.writerow(row)

    print("saved as " + file_name)
