import sys
from collections import deque


def topology_sort():
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for next, dist in graph[now]:
            in_degree[next] -= 1
            anw[next] = max(anw[next], anw[now] + dist)
            print(anw)
            if in_degree[next] == 0:
                q.append(next)
    count = 0
    q.append(end)
    # print(rev_graph)
    while q:
        now = q.popleft()
        for next, dist in rev_graph[now]:
            # print(anw)
            if anw[now] - anw[next] == dist:
                count += 1
                if visit[next] == 0:
                    q.append(next)
                    visit[next] = 1
    print(anw[end])
    # print(visit)
    print(count)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] * (n + 1) for _ in range(n + 1)]
rev_graph = [[] * (n + 1) for _ in range(n + 1)]
in_degree = [0] * (n + 1)
anw = [0] * (n + 1)
visit = [0] * (n + 1)
for _ in range(1, m + 1):
    i, j, road_info = map(int, sys.stdin.readline().split())
    graph[i].append([j, road_info])
    rev_graph[j].append([i, road_info])
    in_degree[j] += 1
start, end = map(int, sys.stdin.readline().split())
topology_sort()


# from collections import deque
#
# n = int(input())  # 노드, 도시 개수
# m = int(input())  # 도로의 개수
# graph = [[] * (n + 1) for _ in range(n + 1)]
# back_graph = [[] * (n + 1) for _ in range(n + 1)]
# indegree = [0] * (n + 1)  # 진입차수
# result = [0] * (n + 1)
# check = [0] * (n + 1)
# q = deque()
# for _ in range(m):
#     a, b, t = map(int, input().split())
#     graph[a].append((b, t))
#     back_graph[b].append((a, t))
#     indegree[b] += 1
# start, end = map(int, input().split())
#
# q.append(start)
#
#
# def topologysort():
#     while q:
#         cur = q.popleft()
#         for i, t in graph[cur]:
#             indegree[i] -= 1
#             result[i] = max(result[i], result[cur] + t)
#             if indegree[i] == 0:
#                 q.append(i)
#
#     # 백트래킹
#     cnt = 0  # 임계경로에 속한 모든 정점의 개수
#     q.append(end)
#     while q:  # 도착점에서 시작점으로
#         cur = q.popleft()
#         for i, t in back_graph[cur]:
#             # 도착점까지의 비용에서 시작점의 비용을 뺐을 때 그 간선비용과 같다면
#             if result[cur] - result[i] == t:
#                 cnt += 1
#                 if check[i] == 0:  # 큐에 한번씩만 담을 수 있도록,중복방문제거
#                     q.append(i)
#                     check[i] = 1
#
#     print(result[end])
#     print(cnt)
#
#
# topologysort()
