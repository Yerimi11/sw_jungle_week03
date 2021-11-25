import sys
import heapq


def dijkstra(s):
    queue = []
    heapq.heappush(queue, (0, s))  # 우선 순위 큐.
    while queue:
        price, current = heapq.heappop(queue)
        if wages[current] < price:  # 처리 했던 곳이면 안감.
            continue
        if current == end:
            print(price)
            exit(0)
        for node in graph[current]:
            next_idx = node[0]
            next_cost = node[1]
            tmp_cost = price + next_cost  # 현재 위치에서 node 까지의 가격
            if tmp_cost < wages[next_idx]:
                wages[next_idx] = tmp_cost
                heapq.heappush(queue, (tmp_cost, next_idx))


inf = 1e8
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
wages = [inf] * (n + 1)

for _ in range(m):
    i, j, cost = map(int, sys.stdin.readline().split())
    graph[i].append((j, cost))

start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(wages[end])
