a, b, v = map(int, input().split())

v -= b
a -= b

print(v // a if v % a == 0 else v // a + 1)
