import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = sorted(map(int, sys.stdin.readline().split()))
    graph[a].append(b)


print(graph)
parent = [1] + [-1] * (n-1)
print(parent)
tmp = deque([1])
while tmp:
    start = tmp.popleft()
    for baby in graph[start]:
        parent[baby] = start
        tmp.append(baby)

        # for k in range(len(graph[baby])):


