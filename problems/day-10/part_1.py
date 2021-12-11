#!/usr/bin/env python3
import sys

sum_ = 0

for line in sys.stdin:
    stack = []
    score = 0
    for c in line:
        if c == ")":
            if not stack or stack.pop() != "(":
                score = 3
                break
        elif c == "]":
            if not stack or stack.pop() != "[":
                score = 57
                break
        elif c == "}":
            if not stack or stack.pop() != "{":
                score = 1197
                break
        elif c == ">":
            if not stack or stack.pop() != "<":
                score = 25137
                break
        else:
            stack.append(c)
    sum_ += score

print(sum_)
