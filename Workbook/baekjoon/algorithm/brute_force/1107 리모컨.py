from dataclasses import asdict


n = input()

origin_number = list(map(int, list(n)))

m = int(input())

btn = []
number = ""

if m != 0:
    removed = list(map(int, input().split()))

for i in range(10):
    if i in removed:
        continue
    btn.append(i)

def find_min(target, btn):
    min_sub = 987654321
    min_num = 0
    for i in btn:
        sub = abs(target - i)
        if sub < min_sub:
            min_sub = sub
            min_num = i
    
    return min_num

cnt = 0

for i in range(len(origin_number)):
    min_num = find_min(origin_number[i], btn)
    number += str(min_num)

number = int("".join(number))

if abs(int(n) - number) < abs(int(n) - 100):
    cnt = len(number)
    abs(int(n) - number)
else:
    print(abs(int(n) - 100))

print(n)