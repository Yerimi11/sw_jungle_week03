# import sys
# from collections import deque
#
# n = int(sys.stdin.readline())
#
# graph = [[] * (n + 1) for _ in range(n + 1)]
#
# for _ in range(n - 1):
#     a, b = sorted(map(int, sys.stdin.readline().split()))
#     graph[a].append(b)
#     graph[b].append(a)
#
# parent = [1] + [-1] * (n - 1)
# tmp = deque([1])
# while tmp:
#     start = tmp.popleft()
#     for baby in graph[start]:
#         if parent[baby - 1] < 0:
#             parent[baby - 1] = start
#             tmp.append(baby)
#
# for i in range(1, len(parent)):
#     print(parent[i])

import sys
sys.setrecursionlimit(10**6)


def dfs(x):
    visit[x] = 1

    for next in graph[x]:
        if visit[next] == 0:
            visit[next] = 1
            parent[next] = x
            dfs(next)


n = int(sys.stdin.readline())
graph = [[] * (n + 1) for _ in range(n + 1)]
parent = [0, 1] + [0] * (n - 1)
visit = [0] * (n + 1)
for _ in range(1, n):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

dfs(1)
# print(parent)
for k in range(2, n + 1):
    print(parent[k])
