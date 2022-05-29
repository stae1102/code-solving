import sys
n, m = map(int, sys.stdin.readline().split())
memo = {}

for i in range(n + m):
    hash_set = sys.stdin.readline().split()
    if len(hash_set) == 2:
        memo[hash_set[0]] = hash_set[1]
    else:
        print(memo[''.join(hash_set)])
