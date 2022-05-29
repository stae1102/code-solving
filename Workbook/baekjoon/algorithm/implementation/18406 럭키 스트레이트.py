n = input()

def solve():
    left = 0
    right = 0
    mid = len(n) // 2
    for i in n[:mid]:
        left += int(i)
    for j in n[mid:]:
        right += int(j)
    if left == right:
        return "LUCKY"
    return "READY"

print(solve())
