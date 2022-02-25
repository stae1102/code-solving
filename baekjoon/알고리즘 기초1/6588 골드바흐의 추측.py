import sys
input = sys.stdin.readline

def is_prime_number(x):
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            return False
    return True

while True:
    num = int(input())
    if num == 0:
        break
    h1, h2 = 3, num - 3
    while h1 <= h2:
        if is_prime_number(h1) and is_prime_number(h2):
            print(f'{num} = {h1} + {h2}')
            break
        else:
            h1 += 2
            h2 -= 2
    else:
        print("Goldbach's conjecture is wrong.")
