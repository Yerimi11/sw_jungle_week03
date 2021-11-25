import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

# print(graph)


def bfs(k):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([])
    queue.append(k)
    while queue:
        x, y = queue.popleft()
        for i_am_stupid in range(4):
            nx = x + dx[i_am_stupid]
            ny = y + dy[i_am_stupid]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print(graph)
                queue.append((nx, ny))
                # print(queue)
                # print(graph)
    return graph[n - 1][m - 1]


# a, b = (0, 0)
# print(a, b)
print(bfs((0, 0)))
