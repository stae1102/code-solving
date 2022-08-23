a, b = map(int, input().split())
c = int(input())

t = a * 60 + b + c

print(t // 60 % 24, t % 60)