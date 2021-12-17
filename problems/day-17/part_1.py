#!/usr/bin/env pypy
import sys

x1, x2 = 70, 96
y1, y2 = -179, -124

highest = 0

for a in range(0, 500):
    for b in range(0, 500):
        x, y = a, b
        xp, yp = 0, 0
        h = 0
        while y1 <= y:
            xp += x
            yp += y
            if x:
                x -= 1
            y -= 1
            h = max(h, yp)
            if x1 <= xp <= x2 and y1 <= yp <= y2:
                highest = max(highest, h)
                break

print(count_)
