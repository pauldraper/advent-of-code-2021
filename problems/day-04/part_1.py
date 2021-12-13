#!/usr/bin/env python3
import sys

draws = list(map(int, next(sys.stdin).split(",")))
next(sys.stdin)

boards = []
board = []
for line in sys.stdin:
    if line == "\n":
        boards.append(board)
        board = []
        continue
    board.append(list(map(int, line.split())))
boards.append(board)

marked = set()


def is_win(board):
    return any(all(c in marked for c in row) for row in board) or any(
        all(row[i] in marked for row in board) for i in range(len(board[0]))
    )


for draw in draws:
    marked.add(draw)
    for i, board in enumerate(boards):
        if is_win(board):
            unmarked = sum(c for row in board for c in row if c not in marked)
            print(unmarked * draw)
            break
    else:
        continue
    break
