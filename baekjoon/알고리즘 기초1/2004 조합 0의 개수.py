import sys
n, m = map(int, sys.stdin.readline().split())

def count_two(x):
    two = 0
    while x > 0:
        x //= 2
        two += x
    return two

def count_five(x):
    five = 0
    while x > 0:
        x //= 5
        five += x
    return five

print(min(count_two(n) - count_two(n - m) - count_two(m), count_five(n) - count_five(n - m) - count_five(m)))
