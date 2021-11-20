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
for i in range(n+1):
    print(graph[i])

dfs(v)
print()
bfs(v)


# a = []
# a += [1]
# a += [2]
# a += [3]
# a.append(4)
# print(a)
#



# from collections import deque
# import sys
#
# read = sys.stdin.readline
#
#
# def bfs(v):
#     q = deque()
#     q.append(v)
#     visit_list[v] = 1
#     while q:
#         v = q.popleft()
#         print(v, end=" ")
#         for i in range(1, n + 1):
#             if visit_list[i] == 0 and graph[v][i] == 1:
#                 q.append(i)
#                 visit_list[i] = 1
#
#
# def dfs(v):
#     visit_list2[v] = 1
#     print(v, end=" ")
#     for i in range(1, n + 1):
#         if visit_list2[i] == 0 and graph[v][i] == 1:
#             dfs(i)
#
#
# n, m, v = map(int, read().split())
#
# graph = [[0] * (n + 1) for _ in range(n + 1)]
# visit_list = [0] * (n + 1)
# visit_list2 = [0] * (n + 1)
#
# for _ in range(m):
#     a, b = map(int, read().split())
#     graph[a][b] = graph[b][a] = 1
#
# dfs(v)
# print()
# bfs(v)
