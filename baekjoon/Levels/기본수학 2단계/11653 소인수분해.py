def find_prime(n: int) -> int:
    prime = 2
    if n == 1:
        return
    while n != 1:
        if n % prime == 0:
            n = int(n / prime)
            print(prime)
        else:
            prime += 1 # 어차피 합성수면 앞서서 나누었기에 소수로밖에 나누어지지 않음

find_prime(int(input()))
