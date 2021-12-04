#!/usr/bin/env python3
import sys

counts = None
lines = 0

for line in sys.stdin:
    lines += 1
    if not counts:
        counts = [0] * len(line.strip())
    for i, digit in enumerate(line.strip()):
        counts[i] += digit == "1"

gamma = int("".join("1" if lines / 2 < c else "0" for c in counts), 2)
epsilon = int("".join("0" if lines / 2 < c else "1" for c in counts), 2)

print(gamma * epsilon)
