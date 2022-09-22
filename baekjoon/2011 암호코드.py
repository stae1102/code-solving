import sys
sys.setrecursionlimit(10**6)
div = 1000000


def find(x):


arr = sys.stdin.readline().rstrip()
l = len(arr)
d = [0] * l

if arr[0] == "0" or "00" in arr:
    print(0)
else:
    print(find(0))
print(d)
