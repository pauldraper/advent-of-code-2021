#!/usr/bin/env pypy3
import itertools
import operator
import sys


def rotate(point, rx, ry, rz):
    x, y, z = point
    for _ in range(rx):
        x, y, z = x, z, -y
    for _ in range(ry):
        x, y, z = z, y, -x
    for _ in range(rz):
        x, y, z = y, -x, z
    return x, y, z


def match(origin_beacons, beacons):
    origin_set = set(origin_beacons)
    for rotation in itertools.product(range(4), repeat=3):
        rotated_beacons = [rotate(b, *rotation) for b in beacons]
        for origin_beacon in origin_beacons:
            for beacon in rotated_beacons:
                offset = tuple(map(operator.sub, origin_beacon, beacon))
                offset_beacons = [
                    tuple(map(operator.add, b, offset)) for b in rotated_beacons
                ]
                if 12 <= len(set(offset_beacons) & origin_set):
                    return [offset_beacons, offset]


scanners = []
for section in sys.stdin.read().strip().split("\n\n"):
    scanner = [tuple(map(int, line.split(","))) for line in section.split("\n")[1:]]
    scanners.append(scanner)


def search(i, beacons, offset):
    answers[i] = offset
    for i, scanner in enumerate(scanners):
        if i in answers:
            continue
        match_ = match(beacons, scanner)
        if match_:
            search(i, match_[0], match_[1])


visited = set()
answers = []


def search(i, beacons, offset):
    answers.append(offset)
    visited.add(i)
    for i, scanner in enumerate(scanners):
        if i in visited:
            continue
        match_ = match(beacons, scanner)
        if match_:
            print("MATCHED", i)
            search(i, match_[0], match_[1])


search(0, scanners[0], (0, 0, 0))

max_ = max(
    sum(map(lambda a, b: abs(a - b), a, b))
    for a, b in itertools.product(answers, repeat=2)
)
print(max_)
