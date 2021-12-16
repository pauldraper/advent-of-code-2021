#!/usr/bin/env python3
import math
import operator
import sys

line = next(sys.stdin).strip()
data = "".join(f"{int(c, 16):04b}" for c in line)

stack = [[]]


def parse(data):
    i = 0
    i += 3
    type_id = int(data[i : i + 3], 2)
    i += 3
    if type_id == 4:
        d = ""
        while True:
            last = data[i] == "0"
            i += 1
            d += data[i : i + 4]
            i += 4
            if last:
                break
        v = int(d, 2)
        stack[-1].append(v)
    else:
        stack.append([])
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
        if type_id == 0:
            v = sum(stack.pop())
        elif type_id == 1:
            v = math.prod(stack.pop())
        elif type_id == 2:
            v = min(stack.pop())
        elif type_id == 3:
            v = max(stack.pop())
        elif type_id == 5:
            v = int(operator.gt(*stack.pop()))
        elif type_id == 6:
            v = int(operator.lt(*stack.pop()))
        elif type_id == 7:
            v = int(operator.eq(*stack.pop()))
        stack[-1].append(v)
    return i


parse(data)

print(stack[0][0])
