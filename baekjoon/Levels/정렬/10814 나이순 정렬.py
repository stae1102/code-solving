import sys
lst = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))]
lst.sort(key = lambda x: int(x.split()[0]))
print("\n".join(lst))
