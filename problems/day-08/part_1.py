#!/usr/bin/env python3
import sys

sum_ = 0

for line in sys.stdin:
    for output in line.split(" | ")[1].split():
        sum_ += len(output) in (2, 3, 4, 7)

print(sum_)
