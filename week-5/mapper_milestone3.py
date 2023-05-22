#!/home/bigdata/anaconda3/bin/python
"""mapper.py"""

import sys
import datetime

A = datetime.datetime.strptime("09:01", "%H:%M")
B = datetime.datetime.strptime("10:00", "%H:%M")
C = datetime.datetime.strptime("10:01", "%H:%M")
D = datetime.datetime.strptime("11:00", "%H:%M")

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, price, payment = data
    if (len(data) == 6):
        dt = datetime.datetime.strptime(time, "%H:%M")
        if (dt >= A) and (dt <= B):
            print(f"09:01-10:00\t1")
        elif (dt >= C) and (dt <= D):
            print(f"10:01-11:00\t1")
