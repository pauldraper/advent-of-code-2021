#!/usr/bin/env python3
import heapq
import sys

data = {
    (i, j): int(v) for i, row in enumerate(sys.stdin) for j, v in enumerate(row.strip())
}
w, h = max(data.keys())
w += 1
h += 1
for (i, j), v in list(data.items()):
    for k in range(5):
        for l in range(5):
            data[(i + k * w, j + l * h)] = (v + k + l - 1) % 9 + 1
end = max(data.keys())

queue = []
heapq.heappush(queue, (-data[(0, 0)], (0, 0)))
visited = set()
while True:
    d, (i, j) = heapq.heappop(queue)
    try:
        v = data[(i, j)]
    except KeyError:
        continue
    if (i, j) in visited:
        continue
    visited.add((i, j))
    d += v
    if (i, j) == end:
        print(d)
        break
    heapq.heappush(queue, (d, (i - 1, j)))
    heapq.heappush(queue, (d, (i + 1, j)))
    heapq.heappush(queue, (d, (i, j - 1)))
    heapq.heappush(queue, (d, (i, j + 1)))
