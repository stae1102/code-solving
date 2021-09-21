import sys
a = sys.stdin.readline().rstrip()
b = a[:]
count = 0

while True:
    count += 1
    if len(b) == 1:
        b = "0" + b
    new = int(b[0]) + int(b[1])
    b = b[1] + str(new)[-1]
    if b[0] == "0":
        b = b[1]
    if b == a:
        print(count)
        break
        
########## 너무 복잡하게 생각했다. 자리수를 나타낼 때는 나머지 연산자와 몫 연산자로 10을 인수로 사용하면 자리수별 값을 추출할 수 있다.

a = int(input())
n = -1
count = 0
while a != n:
    if n == -1: n = a
    n = (n // 10 + n % 10) % 10 + (n % 10) * 10
    count += 1
    
print(count)
