n = int(input())
phase = 1

# 몇 번째 자리 수인지 계산
while True:
    diff = n - (9 * phase * (10 ** (phase - 1)))
    if diff <= 0:
        break
    n = diff
    phase += 1

temp = n // phase
if phase > 1:
    temp += (10 ** (phase - 1)) - 1
remain = n % phase

# n이 1 ~ 9이면 phase는 1 실제 숫자는 1 ~ 9
# n이 10 ~ 189이면 phase는 2 실제 숫자는 10 ~ 99
# n이 190 ~ 2889이면 phase는 3 실제 숫자는 100 ~ 999

if remain > 0:
    temp += 1
    ans = str(temp)[remain - 1]
else:
    ans = str(temp)[-1]

print(ans)