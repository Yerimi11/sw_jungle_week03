import sys

sys.setrecursionlimit(10 ** 8)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    rev_graph[j].append(i)


def dfs(specific_graph, now):
    visit[now] = True
    for next in specific_graph[now]:
        if not visit[next]:
            dfs(specific_graph, next)


count = 0
for i in range(1, n + 1):
    visit = [False] * (n + 1)
    dfs(graph, i)
    if sum(visit) - 1 >= n // 2 + 1:
        count = count + 1
    else:
        visit = [False] * (n + 1)
        dfs(rev_graph, i)
        if sum(visit) - 1 >= n // 2 + 1:
            count = count + 1
print(count)

a = [[] * (n + 1) for _ in range(n + 1)]
b = [[] for _ in range(n+1)]
print(a)
print(b)