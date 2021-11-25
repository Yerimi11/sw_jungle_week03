import sys
from collections import deque
input = sys.stdin.readline
# 정점 갯수, 간선 갯수, 탐색 시작할 정점 번호
Vn, En, v = map(int, input().split())
V = {} # {}: 딕셔너리. 간선이 연결하는 두 정점의 번호가 들어옴(입력값 V[v1], V[v2])
for i in range(1, Vn + 1) : 
    V[i] = [] # 빈 리스트 채워줌 {1: [], 2: [], ...}
for i in range(En) : 
    v1, v2 = map(int, input().split())
    V[v1].append(v2) # V의 ┌ v1(1)번째자리에 v2(2)가 들어감
    V[v2].append(v1) # V: {1: [2], 2: [1], 3:[]...} => 1번 노드는 2번 노드랑 연결되어있고..
for i in range(1, Vn + 1) : 
    V[i].sort()
# print(V) # {1: [2, 5], 2: [1, 3, 5], 3: [2], 4: [7], 5: [1, 2, 6], 6: [5], 7: [4]}


gone = []
def DFS(now) : 
    print(now, end = ' ') # 가장 먼저 자기를 출력
    gone.append(now) # 그리고나서 자기가 갔던 곳에 넣음
    for i in V[now] : # 나우를 갈 수 있는 i에 대해서 i가 아직 안 간 곳이라면 DFS를 실행
        if not i in gone : 
            DFS(i) # 1에서 실행하면 1이 출력되고, 2에서 DFS가 시작돼서 2가 출력되고 4에 대해 DFS가 출력되고 끝남.
DFS(v)              # 그리고 1에서 3도 갈 수 있으니 3에 대해 DFS가 출력됨. 
print()

gone = [] # BFS가 실행될 때 gone을 다시 비워줌.
def BFS(now) : 
    queue = deque()
    queue.append(now) # 큐를 만들고 큐에 나우 하나만 넣음
    while queue : # 큐라는 리스트에 아직 안 간 곳이 추가 됨
        q = queue.popleft() # 사실 덱임 큐처럼 씀
        print(q, end = ' ')
        gone.append(q)
        for i in V[q] : # V: {1: [2,3,4], 2: [1,4], 3:[1,4], 4:[1,2,3]}
            if not i in gone and not i in queue : # 이미 간 곳도 아니고 갈 예정도 아닐 때
                queue.append(i) # que:[] -> que: [2,3,4]
BFS(v)