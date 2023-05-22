#!/home/bigdata/anaconda3/bin/python
"""reducer.py"""

import sys

current_time_interval = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    time_interval, count = line.split("\t")
    try:
        count = int(count)
    except ValueError:
        continue

    if current_time_interval == time_interval:
        current_count += 1
    else:
        if current_time_interval:
            print(f"{current_time_interval}\t{current_count}")
        current_time_interval = time_interval
        current_count = 1

print(f"{current_time_interval}\t{current_count}")
