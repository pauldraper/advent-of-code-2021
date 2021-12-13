#!/usr/bin/env python3
import sys

crabs = list(map(int, next(sys.stdin).split(",")))

min_ = float("inf")

for x in range(min(crabs), max(crabs) + 1):
    min_ = min(min_, sum(abs(c - x) for c in crabs))

print(min_)
