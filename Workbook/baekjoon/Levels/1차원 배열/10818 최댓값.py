l = [int(input()) for _ in range(9)]
print(max(l))
print(l.index(max(l)) + 1)

############## 숏코딩 ##############
print(*max((int(input()),i+1)for i in range(9)))
