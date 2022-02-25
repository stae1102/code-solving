import sys
input = sys.stdin.readline
n = int(input())
binary = []
if n == 0:
    print(0)
    quit()
while n != 0:
    r = int(n % -2)
    if r == -1:
        n = n // -2 + 1    # -11 / -2를 했을 때, 나머지가 -1이 나오게 됨. 따라서 + 1을 해주어야 한다. -11 / -2 의 몫이 6일 때 나머지가 1
        binary.append(1)
    else:
        binary.append(0)
        n //= -2

while len(binary) != 0:
    print(binary.pop(), end='')
