<<<<<<< HEAD
graph = [input() for _ in range(5)]
ans = 0

def solve(x, y, som, yeon):
    global ans
    
    if yeon > 3 or not (0 <= x < 5 and 0 <= y < 5) or visited[x][y]:
        return

    visited[x][y] = True

    if som + yeon == 7:
        print(som, yeon)
        ans += 1
        return
    print(som, yeon)
    if graph[x][y] == 'S':
        som += 1
    else:
        yeon += 1

    solve(x - 1, y, som, yeon)
    solve(x, y - 1, som, yeon)
    solve(x + 1, y, som, yeon)
    solve(x, y + 1, som, yeon)

for i in range(5):
    for j in range(5):
        visited = [[False] * 5 for _ in range(5)]
        solve(i, j, 0, 0)

=======
graph = [input() for _ in range(5)]
ans = 0

def solve(x, y, som, yeon):
    global ans
    
    if yeon > 3 or not (0 <= x < 5 and 0 <= y < 5) or visited[x][y]:
        return

    visited[x][y] = True

    if som + yeon == 7:
        print(som, yeon)
        ans += 1
        return
    print(som, yeon)
    if graph[x][y] == 'S':
        som += 1
    else:
        yeon += 1

    solve(x - 1, y, som, yeon)
    solve(x, y - 1, som, yeon)
    solve(x + 1, y, som, yeon)
    solve(x, y + 1, som, yeon)

for i in range(5):
    for j in range(5):
        visited = [[False] * 5 for _ in range(5)]
        solve(i, j, 0, 0)

>>>>>>> origin/ubuntu
print(ans)