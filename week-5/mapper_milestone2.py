#!/home/bigdata/anaconda3/bin/python
"""mapper.py"""

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, price, payment = data
    if (len(data) == 6):
        if store in ["Atlanta", "Miami", "San Francisco"]:
            print(f"{store}\t{price}\t{item}")
