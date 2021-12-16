#!/usr/bin/env python3
import sys

line = next(sys.stdin).strip()
data = "".join(f"{int(c, 16):04b}" for c in line)

sum_ = 0


def parse(data):
    global sum_
    i = 0
    version_id = int(data[i : i + 3], 2)
    sum_ += version_id
    i += 3
    type_id = int(data[i : i + 3], 2)
    i += 3
    if type_id == 4:
        d = ""
        while True:
            last = data[i] == "0"
            i += 1
            i += 4
            if last:
                break
    else:
        length_type = data[i]
        i += 1
        if length_type == "0":
            length = int(data[i : i + 15], 2)
            i += 15
            j = i + length
            while i < j:
                i += parse(data[i:])
        else:
            n = int(data[i : i + 11], 2)
            i += 11
            for _ in range(n):
                i += parse(data[i:])
    return i


parse(data)

print(sum_)
