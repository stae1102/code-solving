import sys
input = sys.stdin.readline

def is_prime_number(x): # 소수인지 판별하는 함수
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            return False
    return True

for i in range(int(input())):
    n = int(input())
    h1, h2 = int(n / 2), int(n / 2)
    while True:
        if is_prime_number(h1) and is_prime_number(h2):
            print(h1, h2)
            break
        else:
            h1 -= 2
            h2 += 2
            if h1 % 2 == 0: # 짝수면 다시 홀수로 만들어 줌
                h1 += 1
                h2 -= 1
