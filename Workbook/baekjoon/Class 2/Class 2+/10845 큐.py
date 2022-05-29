import sys
from typing import Any
n = int(sys.stdin.readline())

queue = []
idx = 0
capacity = 0

for i in range(n):
    command = sys.stdin.readline().rstrip()

    if "push" in command:
        queue.append((int(list(command.split())[-1])))
        capacity += 1

    elif command == "pop":
        if len(queue) == 0 or idx >= len(queue):
            print(-1)
            continue
        print(queue[idx])
        queue[idx] = 0
        idx += 1
        capacity -= 1
    
    elif command == "size":
        print(capacity)

    elif command == "empty":
        if capacity:
            print(0)
        else:
            print(1)
    
    elif command == "front":
        if capacity == 0:
            print(-1)
            continue
        print(queue[idx])
    
    else:
        if capacity == 0:
            print(-1)
            continue
        print(queue[-1])
