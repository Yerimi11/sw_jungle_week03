import sys
import heapq


# 다익스트라 알고리즘.
# 최단 거리가 k 인 도시를 오름차순으로 출력.

# 준비 : 보드 2개를 만든다.
# (1) graph :
#  - 길이 뚤린 곳을 표시해줄 보드, n + 1 행으로 만들어놔서 1 indexing
#  - 문제 입력값이 아래 처럼 주어지면, graph = [ [], [2,3], [3,4], [], [] ]  <= 1번길과 연결된곳 : 2,3 / 2번길 : 3,4
# 1 2
# 1 3
# 2 3
# 2 4

# (2) cost :
# - 처음에 inf 로 초기화 되어있는 보드, 기능은 목적지에 도착했을때 최단거리의 비용을 입력해줄 보드이다.
# - A-B-E-C : cost = 4로 되어있을 때, A-D-C 길이 있으면 cost = 3 으로 바꿔준다. cost 배열은 1차원이면될듯? 시작도시만 확인하면되니까.

# 시작점부터 배열을 돌며 길이 있는 곳으로 이동한다.


def get_cost(start):
    heap = []
    heapq.heappush(heap, (start, 0))
    cost[start] = 0
    while heap:
        now, tmp_cost = heapq.heappop(heap)
        if cost[now] < tmp_cost:
            continue
        if cost[now] == k:
            continue
        tmp_cost += 1
        for city in graph[now]:
            if cost[city] > tmp_cost:  # 지금 한칸 이동하는 것이므로 + 1 보다 작은지 확인.
                cost[city] = tmp_cost
                heapq.heappush(heap, (city, tmp_cost))
                # print(cost)


inf = 300000  # 하나씩 다 거쳐서 간다고 했을 때, 30만개의 도시가 최대니까 일케하면 될듯?
n, m, k, x = map(int, sys.stdin.readline().split())
count = 0
cost = [inf] * (n + 1)
graph = list([] for _ in range(n + 1))
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
get_cost(x)
if k not in cost:
    print(-1)
else:
    for i in range(1, n + 1):
        if cost[i] == k:
            print(i)

# import sys
# input = sys.stdin.readline
# from collections import deque
# n,m,k,x = map(int,input().split()) #도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
# #x에서 출발하여 거리가 k인 모든 도시를 찾아야 한다
# graph = [[] for _ in range(n+1)]
# answer = [-1] * (n+1)
# answer[x] = 0
# for _ in range(m):
#     a, b = list(map(int,input().split()))
#     graph[a].append(b)
# que = deque([x])
# while que:
#     now = que.popleft()
#     for nxt in graph[now]:
#         if answer[nxt] == -1:
#             answer[nxt] = answer[now] + 1
#             que.append(nxt)
# for i in range(n+1):
#     if answer[i] == k:
#         print(i)
# if k not in answer:
#     print(-1)


# import heapq
# import sys
#
# INF = int(1e9)
# n, m, k, x = map(int, sys.stdin.readline().split())
#
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)
#
# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#
#
# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#
#     while q:
#         dist, now = heapq.heappop(q)
#         if dist > distance[now]:
#             continue
#         for i in graph[now]:
#             cost = dist + 1
#             if cost < distance[i]:
#                 distance[i] = cost
#                 heapq.heappush(q, (cost, i))
#
#
# dijkstra(x)
# flag = 0
# for i in range(1, n + 1):
#     if distance[i] == k:
#         print(i)
#         flag = 1
#
# if flag == 0:
#     print(-1)

#
# import heapq
# import sys
#
# read = sys.stdin.readline
#
#
# def solve():
#     N, M, K, X = map(int, read().split())
#     # 인접 리스트
#     adj = [list() for _ in range(N + 1)]
#     for _ in range(M):
#         f, t = map(int, read().split())
#         adj[f].append(t)
#
#     # 최단 거리 배열
#     min_dists = [300002] * (N + 1)
#
#     # 우선순위 큐
#     # (해당 노드까지의 최단거리, 노드번호) 튜플을 원소로 가짐
#     q = []
#     heapq.heappush(q, (0, X))
#     min_dists[X] = 0
#
#     ans = []
#
#     # 남은 모든 노드들에 대하여
#     while q:
#         # 우선순위 큐 안에 있는 최단 거리 노드 선택
#         dist, node = heapq.heappop(q)
#         # 이미 처리된 노드라면 continue
#         if min_dists[node] < dist:
#             continue
#
#         # 현재 노드까지의 거리가 K라면 정답 리스트에 저장 후 continue
#         if min_dists[node] == K:
#             ans.append(str(node))
#             continue
#
#         # 연결된 노드들의 최단거리 갱신 후 우선순위 큐에 추가
#         for to in adj[node]:
#             if min_dists[to] > dist + 1:
#                 min_dists[to] = dist + 1
#                 heapq.heappush(q, (dist + 1, to))
#
#     return '\n'.join(ans) if ans else -1
#
#
# print(solve())
