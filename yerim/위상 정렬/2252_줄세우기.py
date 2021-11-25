import sys
input = sys.stdin.readline
from collections import deque

Vn, En = map(int, input().split())
parent = [0 for i in range(Vn + 1)]
V = [[] for i in range(Vn + 1)]
for i in range(En) : 
    a, b = map(int, input().split()) # 앞에 숫자가 순서상 앞이니까 big=a
    V[a].append(b) #인접리스트에 삽입
    parent[b] = parent[b] + 1

que = deque()
for i in range(1, Vn + 1) : 
    if parent[i] == 0 : # 부모노드가 없는 애들 먼저 큐에 넣음
        que.append(i) # 1, 2

while que : 
    now = que.popleft()
    print(now, end = ' ')
    for next in V[now] : # now의 인접노드 -> next
        parent[next] = parent[next] - 1 # 간선을 하나씩 지움
        if parent[next] == 0 : # 간선이 0개가 되면
            que.append(next) # 그 숫자로 큐에 넣음 / 마지막에 3 들어가서 que 한 번 더 돔