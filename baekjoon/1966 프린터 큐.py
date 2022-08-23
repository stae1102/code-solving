from sys import stdin
from collections import deque

T = int(stdin.readline())

def printer_queue(m, arr):
    q = deque(arr)
    MAX = max(arr)
    ans = 1

    while True:
        if q[0] == MAX:
            if m == 0:
                return ans
            q.popleft()
            ans += 1
            MAX = max(q)
        else:
            q.append(q.popleft())
        m = m - 1 if m > 0 else len(q) - 1

for _ in range(T):
    n, m = map(int, stdin.readline().split())
    nums = list(map(int, stdin.readline().split()))
    print(printer_queue(m, nums))