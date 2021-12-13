#!/usr/bin/env python3
import sys

counts = [0] * (8 + 1)
for fish in map(int, next(sys.stdin).split(",")):
    counts[fish] += 1

for _ in range(0, 80):
    new_counts = [0] * len(counts)
    for step, count in enumerate(counts):
        if step:
            new_counts[step - 1] += count
        else:
            new_counts[8] += count
            new_counts[6] += count
    counts = new_counts

print(sum(counts))
