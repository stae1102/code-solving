chess = [1, 1, 2, 2, 2, 8]

counter_chess = list(map(int, input().split()))

for idx, val in enumerate(counter_chess):
    chess[idx] -= val

print(*chess)
