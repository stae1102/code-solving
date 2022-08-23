from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

def solve(func, arr):
    rev = False
    for i in func:
        if i == "R":
            if rev: rev = False
            else: rev = True
        else:
            if not arr or not arr[0]: return None
            # 뒤집혔으면 뒤에서 추출
            if rev: arr.pop()
            # 안 뒤집혔으면 앞에서 추출
            else: arr.popleft()

    if rev: arr.reverse()

    return arr

for _ in range(t):
    func = input().rstrip()
    n = int(input())
    q = deque(input().rstrip()[1:-1].split(','))
    q = solve(func, q)
    if q != None: print("[" + ','.join(q) + "]")
    else: print('error')