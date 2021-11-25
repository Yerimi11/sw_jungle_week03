# import sys
#
# sys.setrecursionlimit(10 ** 4)
#
#
# def dfs(x):
#     visited[x] = 1
#     for k in range(1, n + 1):
#         if visited[k] == 0 and graph[x][k] == 1:
#             dfs(k)
#
#
# n = int(sys.stdin.readline())
# c = int(sys.stdin.readline())
# visited = [0] * (n + 1)
# graph = list([0] * (n + 1) for _ in range(n + 1))
# for _ in range(c):
#     i, j = map(int, sys.stdin.readline().split())
#     graph[i][j] = graph[j][i] = 1
#
# dfs(1)
# print(sum(visited) - 1)


import sys


def dfs(x):
    global count
    visit[x] = 1
    for next in graph[x]:
        if visit[next] == 0:
            count += 1
            dfs(next)


n = int(sys.stdin.readline())
graph = [[] * (n + 1) for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(1, int(sys.stdin.readline()) + 1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

count = 0
dfs(1)
print(count)

