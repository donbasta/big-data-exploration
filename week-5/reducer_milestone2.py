#!/home/bigdata/anaconda3/bin/python
"""reducer.py"""

import sys

current_store = None
current_max_price = 0
item_with_max_price = None

for line in sys.stdin:
    line = line.strip()
    store, price, item = line.split("\t")
    try:
        price = float(price)
    except ValueError:
        continue

    if current_store == store:
        if price > current_max_price:
            current_max_price = price
            item_with_max_price = item
    else:
        if current_store:
            print(f"{current_store}\t{current_max_price}\t{item_with_max_price}")
        current_store = store
        current_max_price = price
        item_with_max_price = item

print(f"{current_store}\t{current_max_price}\t{item_with_max_price}")
