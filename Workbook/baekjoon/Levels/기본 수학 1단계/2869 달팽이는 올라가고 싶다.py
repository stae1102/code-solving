import math

up, down, top = map(int, input().split())

def climb(u: int, d: int, t: int) -> int:
    if u == t:
        return 1
    return math.ceil((t - u) / (u - d)) + 1

print(climb(up, down, top))

#######################

"""
1)
4 + 2 * (x - 1) < 6
(x - 1) * 2 < 2

2)
5 + 3 * (x - 1) < 12
3 * (x - 1) < 7
x - 1 < 7 / 3
x < 2.xx + 1
x < 3.xx

100 + 1 * (x - 1) < 1000000000
x - 1  < 999999900
x < 999999901

u + (u - d) * (day - 1) = t
(u - d) * (day - 1) = t - u
day = (t - u) / (u - d) + 1

처음 날은 u만 들어가기 때문에 day - 1로 조절하여 걸린 날을 계산해 주어야 한다.
또한, (t - u) / (u - d) 가 소수로 나오면 올림해줘야 하기 때문에 ceil을 사용했다.
"""
