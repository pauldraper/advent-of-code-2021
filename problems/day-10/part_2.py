#!/usr/bin/env python3
import sys

scores = []

for line in sys.stdin:
    stack = []
    for c in line.strip():
        if c == ")":
            if not stack or stack.pop() != "(":
                break
        elif c == "]":
            if not stack or stack.pop() != "[":
                break
        elif c == "}":
            if not stack or stack.pop() != "{":
                break
        elif c == ">":
            if not stack or stack.pop() != "<":
                break
        else:
            stack.append(c)
    else:
        score = 0
        for c in reversed(stack):
            score = score * 5 + "([{<".index(c) + 1
        scores.append(score)


scores.sort()

print(scores[len(scores) // 2])
