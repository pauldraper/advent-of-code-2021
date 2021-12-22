#!/usr/bin/env pypy3
import sys

ins = []
xs = []
ys = []
zs = []

for line in sys.stdin:
    status, positions = line.split()
    x, y, z = positions.split(",")
    x1, x2 = map(int, x.split("=")[1].split(".."))
    y1, y2 = map(int, y.split("=")[1].split(".."))
    z1, z2 = map(int, z.split("=")[1].split(".."))
    ins.append((status == "on", (x1, x2), (y1, y2), (z1, z2)))
    xs.append(x1)
    xs.append(x2 + 1)
    ys.append(y1)
    ys.append(y2 + 1)
    zs.append(z1)
    zs.append(z2 + 1)

ins.reverse()
xs.sort()
ys.sort()
zs.sort()

count = 0

for x1, x2 in zip(xs, xs[1:]):
    print(f"x={x1}")
    ins_x = [(a, x, y, z) for a, x, y, z in ins if x[0] <= x1 <= x[1]]
    for y1, y2 in zip(ys, ys[1:]):
        ins_y = [(a, x, y, z) for a, x, y, z in ins_x if y[0] <= y1 <= y[1]]
        for z1, z2 in zip(zs, zs[1:]):
            if next((a for a, x, y, z in ins_y if z[0] <= z1 <= z[1]), False):
                count += (x2 - x1) * (y2 - y1) * (z2 - z1)

print(count)
