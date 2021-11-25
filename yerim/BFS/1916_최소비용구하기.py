import sys
input = sys.stdin.readline
import heapq

Vn = int(input())
En = int(input())
V = {}
for i in range(1, Vn + 1) : 
    V[i] = []
for i in range(En) : 
    v1, v2, cost = map(int, input().split())
    V[v1].append([v2, cost])
start, end = map(int, input().split()) # m+2줄 다음 입력값

maxc = float('inf') # 무한대를 넣어두고 최솟값 갱신할거임
min_cost = [maxc for i in range(Vn + 1)] # inf로 가득찬 min_cost배열 만듦 / min_cost: [inf, inf, inf,.. Vn+1만큼]

def DIJK(start) : 
    min_cost[start] = 0 # min_cost배열 [start]인덱스에 0을 넣음 / min_cost: [inf, 0, inf, ..]
    heap = [[0, start]] # 힙을 만듦(다익스트라 라서!!) / heap: [[0, 1]] 초기값 / [거리, 노드] : 거리를 기준으로 정렬할거라서
    while heap : 
        cost2, node = heapq.heappop(heap) # [0, 1] 초기값 / 1 pop -> 1 탐색
        if cost2 <= min_cost[node] : # 0 <= 0 / # 현재 노드의 저장된 최솟값과 리스트에서 받아온 거리값과 비교해서 받은 값이 작을 경우 리스트 업데이트
            for next in V[node] : # 인접노드 [2,2] [3,3] [4,1] 덩어리.. / 다음노드, 거리 (힙 들어갈 때 거리 기준으로 들어가니까 원래 입력값하고 순서 바뀜)
                if cost2 + next[1] < min_cost[next[0]] : # 뭐가 더 작은지 최솟값 비교 (시작점~현재노드 거리(0) + 현재노드~다음노드 거리(2) << 최솟값 리스트의 최솟값(inf))
                    min_cost[next[0]] = cost2 + next[1] # 최솟값 갱신
                    heapq.heappush(heap, [cost2 + next[1], next[0]])
DIJK(start)
print(min_cost[end])