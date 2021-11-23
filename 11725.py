import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [[] * (n + 1) for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = sorted(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)

parent = [1] + [-1] * (n - 1)
tmp = deque([1])
while tmp:
    start = tmp.popleft()
    for baby in graph[start]:
        if parent[baby - 1] < 0:
            parent[baby - 1] = start
            tmp.append(baby)

for i in range(1, len(parent)):
    print(parent[i])
