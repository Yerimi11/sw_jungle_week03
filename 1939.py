import sys
import heapq


def dijkstra(sp, ep):
    q = []
    heapq.heappush(q, (0, sp))
    while q:
        dist, now = heapq.heappop(q)
        dist = dist * -1

        if now == ep:
            print(dist)
            break
        if distance[now] > dist:
            continue
        for cost, next in graph[now]:
            if dist == 0:
                distance[next] = cost
                heapq.heappush(q, (-distance[next], next))
            elif distance[next] < cost and distance[next] < dist:
                distance[next] = min(dist, cost)
                heapq.heappush(q, (-distance[next], next))


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

distance = [0] * (n + 1)
start, end = map(int, sys.stdin.readline().split())

dijkstra(start, end)
