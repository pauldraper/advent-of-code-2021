#!/usr/bin/env python3
import collections
import sys

conn = collections.defaultdict(list)
for line in sys.stdin:
    a, b = line.strip().split("-")
    conn[a].append(b)
    conn[b].append(a)


def visit(start, depth=0, visited=collections.defaultdict(int)):
    if depth > 100:
        return 0
    total = 0
    if start.islower():
        visited[start] += 1
    for c in conn[start]:
        if c == "start":
            continue
        if c == "end":
            total += 1
        elif visited[c] < 2 - any(n == 2 for n in visited.values()):
            total += visit(c, depth + 1, visited)
    if start.islower():
        visited[start] -= 1
    return total


print(visit("start"))
