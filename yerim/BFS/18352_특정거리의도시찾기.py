import sys
from collections import deque
input = sys.stdin.readline

v, e, cost, start = map(int, input().split())
graph = [[] for _ in range(v+1)] 
for _ in range(e):
    # graph에 인접 리스트로 인풋 받기
    a, b = map(int, input().split())
    if b == start:
        continue
    # a에서 출발해서 b로 도착한다
    graph[a].append(b) # 단방향

    # 방문 체크 리스트 (거리를 갱신)
    checklist = [0 for _ in range(v+1)]
    result = []

def BFS(start) : # 시작값 받아옴
    # 초깃값 넣기
    queue = deque()
    queue.append(start) # 큐를 만들고 큐에 start 하나만 넣음

    # 큐(덱)이 빌 때 까지 돌린다
    while queue : 
        q = queue.popleft() # 큐의 맨 앞에 있는 노드 선택
        # q랑 인접한 노드들만 가져오는 리스트(그래프)
        for next in graph[q] : # graph: {1: [2,3,4], 2: [1,4], 3:[1,4], 4:[1,2,3]}
            if checklist[next] == 0: # 이미 간 곳이 아닐 때
                queue.append(next) # que:[] -> que: [2,3,4]
                checklist[next] = checklist[q] + 1 # 내 위치+1해서 다음노드의 거리값을 줌

                if checklist[next] == cost: # 만약 그 거리가 내가 가려는 거리와 같으면
                    result.append(next)
BFS(start)

result.sort()
for node in result:
    print(node)

if not result: # result가 비어있는 경우라면
    print(-1)

