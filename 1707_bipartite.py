# 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할가능. > 이분그래프(Bipartite graph)

# dfs 로 색칠만하고, 인접행렬과 색깔이 같은지 for 문으로 돌면 더 쉬움

import sys
sys.setrecursionlimit(10**6)


def dfs(x):
    global flag
    visit[x] = 1
    for next in graph[x]:
        if visit[next] == 0:
            check[next] = False if check[x] else True
            dfs(next)
        else:
            if check[x] == check[next]:
                flag = False
                return


t = int(sys.stdin.readline())
anw = []

for _ in range(t):
    v, e = map(int, sys.stdin.readline().split())
    check = [False, True] + [False] * (v - 1)
    visit = [0] * (v + 1)
    flag = True
    graph = [[] * (v + 1) for _ in range(v + 1)]
    for _ in range(1, e + 1):
        i, j = map(int, sys.stdin.readline().split())
        graph[i].append(j)
        graph[j].append(i)
    for i in range(1, v+1):
        if not visit[i]:
            dfs(i)
    anw.append("YES" if flag else "NO")

for case in anw:
    print(case)
