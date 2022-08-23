from sys import stdin
from collections import deque

T = int(stdin.readline())


def solve(coms, arr):
    shift = False
    arr = deque(arr)
    for com in coms:
        if com == "R":
            shift = False if shift == True else True
        else:
            if not arr or not arr[0]:
                return "error"
            if shift:
                arr.pop()
            else:
                arr.popleft()

    if shift:
        return reversed(arr)
    else:
        return arr


for _ in range(T):
    commands = stdin.readline().rstrip()
    n = stdin.readline()
    _arr = stdin.readline().lstrip('[').rstrip(']\n').split(',')
    ans = solve(commands, _arr)
    if ans == "error":
        print(ans)
    else:
        print("[" + ','.join(ans) + "]")
