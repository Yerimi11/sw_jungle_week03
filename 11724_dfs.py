import sys

sys.setrecursionlimit(10 ** 5)
v, e = map(int, sys.stdin.readline().split())
graph = [list([0] * (v + 1)) for _ in range(v + 1)]
visited = list([0] * (v + 1))
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1


def dfs(x):
    visited[x] = 1
    for i in range(1, v + 1):
        if visited[i] == 0 and graph[x][i] == 1:
            dfs(i)


count = 0
for i in range(1, v + 1):
    dx = sum(visited)
    if dx == v:
        print(count)
        exit(0)
    dx_ = sum(visited)
    if dx != dx_:
        count += 1

print(count)
