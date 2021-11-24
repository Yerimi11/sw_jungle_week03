import sys
from collections import deque
input = sys.stdin.readline

v, e, cost, start = map(int, input().split())
graph = [[] for _ in range(v+1)] 
for _ in range(e):
    # graph에 인접 리스트로 인풋 받기
    a, b = map(int, input().split())
    # a에서 출발해서 b로 도착한다
    graph[a].append(b) # 단방향

    # 방문 체크 리스트
    checklist = [0 for _ in range(v+1)]


gone = [] # BFS가 실행될 때 gone을 다시 비워줌. 
def BFS(now) : 
    que = [now] # 큐를 만들고 큐에 나우 하나만 넣음
    while que : # 큐라는 리스트에 아직 안 간 곳이 추가 됨
        q = que[0]
        print(q, end = ' ')
        gone.append(q)
        del que[0] 
        for i in V[q] : # V: {1: [2,3,4], 2: [1,4], 3:[1,4], 4:[1,2,3]}
            if not i in gone and not i in que : # 이미 간 곳도 아니고 갈 예정도 아닐 때
                que.append(i) # que:[] -> que: [2,3,4]
BFS(v)