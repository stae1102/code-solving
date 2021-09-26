sugar = int(input())

def pack(a: int) -> int:
    i = 0 # 3kg 봉투 0개
    while True:
        if (a - (3 * i)) % 5  == 0: # 3kg 봉투의 개수를 늘리며 5kg의 봉투를 최대화
            if a - (3 * i) < 0:
                return -1 # 불가능한 경우!
            return (a - (3 * i)) // 5 + i if a - (3 * i) != 0 else i # 3으로 나누어 떨어지면 3kg만 사용하니까
        i += 1

print(pack(sugar))
