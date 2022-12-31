from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
buffer = deque()
size = 0

while True:
  command = int(input())
  if command == -1:
    break
  elif command == 0:
    buffer.popleft()
    size -= 1
  else:
    if size != n:
      buffer.append(command)
      size += 1

if size != 0:
  print(*buffer)
else:
  print('empty')