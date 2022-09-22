import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())


def check_team(k):  # k: 현재 노드
    global cnt

    visited[k] = True
    next = member[k]

    if not visited[next]:  # 아직 방문하지 않았다면
        check_team(next)

    elif not done[next]:
        j = next
        while j != k:
            cnt += 1
            j = member[j]
        cnt += 1

    done[k] = True  # 현재 노드는 완료 처리


for _ in range(t):
    n = int(input())
    member = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    done = [False] * (n + 1)

    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            check_team(i)

    print(n - cnt)
