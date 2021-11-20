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


def dfs(n):
    Heap.append(n)
    for v in V[n]:
        if v not in Heap:
            dfs(v)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

V = [[] for _ in range(N + 1)]
Heap = []

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    V[a].append(b)
    V[b].append(a)
if V:
    print("zz")
dfs(1)

print(len(Heap) - 1)