n = input()

phase = len(n)

cnt = 0

for i in range(phase - 1):
    cnt += 9 * (10 ** i) * (i + 1)

print(cnt + (int(n) - 10 ** (phase - 1) + 1) * phase)