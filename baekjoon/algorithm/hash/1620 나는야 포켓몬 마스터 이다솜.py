import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocket = {}

for i in range(n):
    k = input().rstrip()
    pocket[str(i + 1)] = k
    pocket[k] = i + 1

for _ in range(m):
    q = input().rstrip()
    print(pocket[q])
