# n 제곱 바둑판
# 검은방/흰방
# 검은방 = 벽
# (1,1) -> 항상 흰방
# (n+1,n+1) -> 항상 흰방
# 검은방을 흰방으로 바꾸는 것을 최소화하여 끝방 도착.
# 안바꿔도 되면 0

# idea ->
# 0의 개수 세기?


import sys
from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visit[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for _ in range(4):
            nx = dx[_] + x
            ny = dy[_] + y
            if nx <= 0 or nx > n or ny <= 0 or ny > n or visit[nx][ny] != -1:
                continue
            # 들리지 않은 곳일때, 검은 방이면 1을 더해준다.
            if graph[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                print(visit)
                queue.append((nx, ny))
            else:
                visit[nx][ny] = visit[x][y]
                queue.appendleft((nx, ny))


n = int(sys.stdin.readline())
graph = [[0] * (n + 1)] + [[0] + list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visit = list([-1] * (n + 1) for _ in range(n + 1))

bfs(1, 1)
print(visit[n][n])

# ##### 문제 #####
# # n×n 바둑판 모양으로 총 n2개의 방이 있다.
# # 일부분은 검은 방이고 나머지는 모두 흰 방이다.
# # 검은 방은 사면이 벽으로 싸여 있어 들어갈 수 없다.
# # 서로 붙어 있는 두 개의 흰 방 사이에는 문이 있어서 지나다닐 수 있다.
# # 윗줄 맨 왼쪽 방은 시작방으로서 항상 흰 방이고,
# # 아랫줄 맨 오른쪽 방은 끝방으로서 역시 흰 방이다.
# # 시작방에서 출발하여 길을 찾아서 끝방으로 가는 것이 목적인데,
# # 아래 그림의 경우에는 시작방에서 끝 방으로 갈 수가 없다.
# # 부득이 검은 방 몇 개를 흰 방으로 바꾸어야 하는데 되도록 적은 수의 방의 색을 바꾸고 싶다.
# # 검은 방에서 흰 방으로 바꾸어야 할 최소의 수를 구하는 프로그램을 작성하시오.
# # 단, 검은 방을 하나도 흰방으로 바꾸지 않아도 되는 경우는 0이 답이다.
#
# ##### 입력 #####
# # 첫 줄에는 한 줄에 들어가는 방의 수 n(1 ≤ n ≤ 50)이 주어지고,
# # 다음 n개의 줄의 각 줄마다 0과 1이 이루어진 길이가 n인 수열이 주어진다.
# # 0은 검은 방, 1은 흰 방을 나타낸다.
#
# ##### 출력 #####
# # 첫 줄에 흰 방으로 바꾸어야 할 최소의 검은 방의 수를 출력한다.
#
# import sys, heapq
#
# room_size = int(sys.stdin.readline().rstrip())
# room_info = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(room_size)]
# # for room in room_info:
# #     print(room)
#
# visited = [[0] * room_size for _ in range(room_size)]
#
#
# def DIJKSTRA():
#     heap = []
#     heapq.heappush(heap, [0, 0, 0])
#     visited[0][0] = 1
#     while heap:
#         change_count, now_x, now_y = heapq.heappop(heap)
#         if now_x == room_size - 1 and now_y == room_size - 1:
#             print(change_count)
#             return
#         for dir_x, dir_y in (-1, 0), (1, 0), (0, -1), (0, 1):
#             new_x, new_y = now_x + dir_x, now_y + dir_y
#
#             if 0 <= new_x < room_size and 0 <= new_y < room_size and visited[new_x][new_y] == 0:
#                 visited[new_x][new_y] = 1
#                 if room_info[new_x][new_y] == 0:
#                     heapq.heappush(heap, [change_count + 1, new_x, new_y])
#                 else:
#                     heapq.heappush(heap, [change_count, new_x, new_y])
#
#
# DIJKSTRA()