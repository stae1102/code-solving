import sys
input = sys.stdin.readline
INF = float('inf')


def bf(start):
    distance[start] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            if distance[cur] != INF and distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n - 1:
                    return True

    return False


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

distance = [INF] * (n + 1)

if bf(1):
    print(-1)
else:
    for i in range(2, n + 1):
        print(distance[i] if distance[i] != INF else -1)
