#!/usr/bin/env python3
import sys

horizonal = 0
depth = 0

for line in sys.stdin:
    direction, dist = line.split(" ")
    if direction == "forward":
        horizonal += int(dist)
    elif direction == "up":
        depth -= int(dist)
    elif direction == "down":
        depth += int(dist)

print(horizonal * depth)
