import sys
import collections

for i in range(int(sys.stdin.readline())):
    n, idx = map(int, sys.stdin.readline().split())
    queue = collections.deque(map(int, sys.stdin.readline().split()))
    
    cnt = 1
    m = max(queue)
    while True:
        if queue[0] != m:
            queue.append(queue.popleft())
        else:
            if idx == 0:
                break
            queue.popleft()
            cnt += 1
            m = max(queue)
        idx -= 1
        if idx < 0:
            idx = len(queue) - 1
    print(cnt)
