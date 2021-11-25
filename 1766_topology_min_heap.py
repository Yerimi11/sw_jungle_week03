import sys
from heapq import heappop, heappush


def topology_sort():
    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heappush(heap, i)

    while heap:
        now = heappop(heap)
        anw.append(now)
        for k in graph[now]:
            in_degree[k] -= 1
            if in_degree[k] == 0:
                heappush(heap, k)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for i in range(n + 1)]
in_degree = [0] * (n + 1)
anw = []

for _ in range(1, m + 1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    in_degree[j] += 1

topology_sort()
print(*anw)
