import sys
from collections import deque


def bfs(p):
    queue = deque()
    queue.append(p)
    visited_[p] = 1
    while queue:
        p = queue.popleft()
        print(p, end=" ")
        for idx in range(1, n + 1):
            if visited_[idx] == 0 and graph[p][idx] == 1:
                queue.append(idx)
                visited_[idx] = 1


def dfs(q):
    visited[q] = 1
    print(visited)
    print(q, end=" ")
    for idx in range(1, n + 1):
        if visited[idx] == 0 and graph[q][idx] == 1:
            dfs(idx)


n, m, v = map(int, sys.stdin.readline().split())
visited = [0] * (n + 1)
visited_ = [0] * (n + 1)
graph = list(list(0 for _ in range(n + 1)) for _ in range(n + 1))
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i][j] = graph[j][i] = 1
for i in range(n + 1):
    print(graph[i])

dfs(v)
print()
bfs(v)
