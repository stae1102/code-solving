a, p = map(int, input().split())

prev = a

d = [0] * 295246
d[a] = 1

def calc(num):
    temp = 0
    while num > 0:
        temp += (num % 10) ** p
        num //= 10
    temp += num ** p
    return temp

while True:
    next = calc(prev)
    # print(next)
    
    if d[next] != 0:
        print(d[next] - 1)
        break

    d[next] = d[prev] + 1
    prev = next