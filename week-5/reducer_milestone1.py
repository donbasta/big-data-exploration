#!/home/bigdata/anaconda3/bin/python
"""reducer.py"""

import sys

current_item = None
current_total_price = 0

for line in sys.stdin:
    line = line.strip()
    item, price = line.split("\t")
    try:
        price = float(price)
    except ValueError:
        continue
    
    if current_item == item:
        current_total_price += price
    else:
        if current_item:
            print(f"{current_item}\t{current_total_price}")
        current_total_price = price
        current_item = item

print(f"{current_item}\t{current_total_price}")
