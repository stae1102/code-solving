sugar = int(input())

def pack(a: int) -> int:
    i = 0 # 3kg 봉투 0개
    while True:
        if (a - (3 * i)) % 5  == 0:
            if a - (3 * i) < 0:
                return -1
            return (a - (3 * i)) // 5 + i if a - (3 * i) != 0 else i
        i += 1

print(pack(sugar))