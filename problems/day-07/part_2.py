#!/usr/bin/env python3
import sys

data = list(map(int, next(sys.stdin).split(",")))

d = sum(data) / len(data)

l = []
for x in range(min(data), max(data) + 1):
    l.append(sum(abs(a - x) * (abs(a - x) + 1) / 2 for a in data))

print(min(l))
