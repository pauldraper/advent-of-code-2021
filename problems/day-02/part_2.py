#!/usr/bin/env python3
import sys

horizontal = 0
aim = 0
depth = 0

for line in sys.stdin:
    direction, dist = line.split(" ")
    if direction == "forward":
        horizontal += int(dist)
        depth += aim * int(dist)
    elif direction == "up":
        aim -= int(dist)
    elif direction == "down":
        aim += int(dist)

print(horizontal * depth)
