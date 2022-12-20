from collections import Counter
n = int(input())

int_arr = Counter(list(map(int, input().split())))

print(int_arr[int(input())])
