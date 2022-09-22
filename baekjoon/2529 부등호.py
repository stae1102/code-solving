import sys
input = sys.stdin.readline


def solve(idx):  # idx는 부등호 위치, num은 들어갈 수
    if idx == k + 1:
        _num = ''.join(map(str, tmp))
        ans.append(_num)
        return

    for i in range(10):
        if not i in tmp:
            if idx == 0 or (opers[idx] == ">" and tmp[-1] > i) or (opers[idx] == "<" and tmp[-1] < i):
                tmp.append(i)
                solve(idx + 1)
                tmp.pop()


k = int(input())
opers = [""] + input().rstrip().split()
tmp = []

ans = []

solve(0)

print(ans[-1])
print(ans[0])
