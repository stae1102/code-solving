a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = A.union(B)
D = A.intersection(B)

print(len(C.difference(D)))