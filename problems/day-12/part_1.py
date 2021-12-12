#!/usr/bin/env python3
import collections
import sys

conn = collections.defaultdict(list)
for line in sys.stdin:
    a, b = line.strip().split("-")
    conn[a].append(b)
    conn[b].append(a)


def visit(start, depth=0, visited=set()):
    if depth > 100:
        return 0
    total = 0
    if start.islower():
        visited.add(start)
    for c in conn[start]:
        if c == "end":
            total += 1
        elif c not in visited:
            total += visit(c, depth + 1, visited)
    if start.islower():
        visited.remove(start)
    return total


print(visit("start"))
