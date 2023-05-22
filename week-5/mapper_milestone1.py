#!/home/bigdata/anaconda3/bin/python
"""mapper.py"""

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, price, payment = data
    if (len(data) == 6):
        if item == "Toys":
            print(f"{item}\t{price}")
        if item == "Consumer Electronics":
            print(f"{item}\t{price}")
