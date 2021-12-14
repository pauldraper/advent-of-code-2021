#!/usr/bin/env python3
import collections
import sys

data = next(sys.stdin).strip()
next(sys.stdin)
rules = dict(line.strip().split(" -> ") for line in sys.stdin)

for _ in range(10):
    new_data = ""
    for i, c in enumerate(data[:-1]):
        new_data += c
        try:
            new = rules[data[i : i + 2]]
        except KeyError:
            pass
        new_data += new
    data = new_data + data[-1]

result = collections.Counter(data)
max_ = max(result.values())
min_ = min(result.values())

print(max_ - min_)
