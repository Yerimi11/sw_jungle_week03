import sys
from collections import deque, defaultdict


def bfs():
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    for pp in range(len(virus)):
        for corona in virus[pp]:
            q.append(corona)

    tmp = len(q)
    while q and count < time:

        x, y = q.popleft()
        tmp -= 1
        if tmp == 0:
            tmp = len(q)
            count += 1
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and visit[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    visit[nx][ny] = 1
                    q.append((nx, ny))


n, k = map(int, sys.stdin.readline().split())
graph = list([] * n for _ in range(n))
visit = list([0] * n for _ in range(n))
for _ in range(n):
    graph[_] = list(map(int, sys.stdin.readline().split()))
# virus = [[] * (n**2) for _ in range(n**2)]
virus = defaultdict(list)
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0:
            idx = graph[i][j] - 1
            virus[idx].append((i, j))

time, X, Y = map(int, sys.stdin.readline().split())
count = 0
bfs()
print(graph[X - 1][Y - 1])