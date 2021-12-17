#!/usr/bin/env pypy
import sys

x1, x2 = 70, 96
y1, y2 = -179, -124

count_ = 0

for a in range(0, 500):
    for b in range(-500, 500):
        x, y = a, b
        xp, yp = 0, 0
        highest = 0
        while y1 <= y:
            xp += x
            yp += y
            if x:
                x -= 1
            y -= 1
            highest = max(highest, yp)
            if x1 <= xp <= x2 and y1 <= yp <= y2:
                count_ += 1
                break

print(count_)
