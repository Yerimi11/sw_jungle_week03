# # 그래프 이론
# # 그래프 탐색
# # 너비 우선 탐색
#
# # 시간 제한	메모리 제한	제출	    정답	    맞힌사람	정답비율
# # 1 초	    128 MB	    33052	10951	7428	31.321%
# # 골드 IV
#
# # 문제 :
# # 사악한 암흑의 군주 이민혁, 사혼의 구슬 획득, 티떱숲 홍수일으키려함.
# # 고슴도치 한마리 친한친구 비버의 굴로 도망가서 홍수를 피하려고함.
# # 지도 R행 C열.
# # '.' == empty, '*' == flooded, barrier = 'X'
# # 비버의굴을 D, 고슴도치 위치는 S
# # 매분마다 동서남북 한칸 이동, 홍수도 인접 '.' 으로 매분 확장됨.
# # 돌은 둘다 못감.
# # 고슴도치는 물로 못가고, 물도 비버로 못감.
# # 고슴도치가 비버의 굴로 갈 수 있는 최소시간.
# # 다음에 물이 찰 곳으로도 이동 못함.
#
# import sys
# from collections import deque
#
#
# def simulation(holy, shit):
#     global count
#     while shit:
#         if holy:
#             tmp = holy.copy()
#             holy.popleft()
#             while tmp:
#                 x, y = tmp.popleft()
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     if 0 <= nx < r and 0 <= ny < c:
#                         if graph[nx][ny] != 'D':
#                             if graph[nx][ny] != 'X':
#                                 graph[nx][ny] = "X"
#                                 holy.append((nx, ny))
#                                 graph[x][y] = 'X'
#         k = 0
#         flag = False
#         hox, hoy = shit.popleft()
#         for i in range(4):
#             hox_ = hox + dx[i]
#             hoy_ = hoy + dy[i]
#             if 0 <= hoy_ < c and 0 <= hox_ < r:
#                 if graph[hox_][hoy_] == 'D':
#                     print(count + 1)
#                     exit(0)
#                 if graph[hox_][hoy_] == 'X' or graph[hox_][hoy_] == '*':
#                     k += 1
#                 else:
#                     graph[hox_][hoy_] = 'S'
#                     flag = True
#                     shit.append((hox_, hoy_))
#                     graph[hox][hoy] = 'X'
#         if flag:
#             count += 1
#     print(word)
#
#
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# word = "KAKTUS"
# r, c = map(int, sys.stdin.readline().split())
# # r, c <= 50
# graph = [[] * c for _ in range(r)]
# bieber = 0
# hog = 0
# stone = []
# flooded = deque()
# for _ in range(r):
#     road_info = sys.stdin.readline().rstrip()
#     if 'X' in road_info:
#         stone.append((_, road_info.index('X')))
#     if 'S' in road_info:
#         hog = (_, road_info.index('S'))
#     if 'D' in road_info:
#         bieber = (_, road_info.index('D'))
#     if '*' in road_info:
#         flooded.append((_, road_info.index('*')))
#     graph[_] = list(road_info)
# # print(bieber, hog, flooded, stone)
# # print(graph)
#
# q = deque()
# q.append(hog)
# # flooded.append((1, 2))
# # k = deque()
# # k.extend(flooded)
# # print(k)
# # print(flooded)
# count = 0
# simulation(flooded, q)
#
# # a = 1
# # print(type(a == 2 or 1))
# # a = 'D...*.'
# # a[1] = '1'
# # print(a[1])

# import sys
# from collections import deque
#
#
# def simulation():
#     global count
#     while shit:
#         if holy:
#             tmp = holy.copy()
#             holy.popleft()
#             while holy:
#                 x, y = tmp.popleft()
#                 for i in range(4):
#                     nx = x + dx[i]
#                     ny = y + dy[i]
#                     if 0 <= nx < r and 0 <= ny < c:
#                         if graph[nx][ny] != 'D':
#                             if graph[nx][ny] != 'X':
#                                 graph[nx][ny] = "X"
#                                 holy.append((nx, ny))
#                                 graph[x][y] = 'X'
#         flag = False
#         hox, hoy = shit.popleft()
#         for i in range(4):
#             hox_ = hox + dx[i]
#             hoy_ = hoy + dy[i]
#             if 0 <= hoy_ < c and 0 <= hox_ < r:
#                 if graph[hox_][hoy_] == 'D':
#                     print(count + 1)
#                     exit(0)
#                 if graph[hox_][hoy_] != 'X' and graph[hox_][hoy_] != '*':
#                     graph[hox_][hoy_] = 'S'
#                     flag = True
#                     shit.append((hox_, hoy_))
#                     graph[hox][hoy] = 'X'
#         if flag:
#             count += 1
#     print("KAKTUS")
#
#
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
# r, c = map(int, sys.stdin.readline().split())
# graph = [[] * c for _ in range(r)]
# holy = deque()
# shit = deque()
#
# for _ in range(r):
#     road_info = sys.stdin.readline().rstrip()
#     if 'S' in road_info:
#         shit.append((_, road_info.index('S')))
#     if '*' in road_info:
#         holy.append((_, road_info.index('*')))
#     graph[_] = list(road_info)
#
# count = 0
# simulation()

import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())
tw = []
q = deque()
tmp = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(r):
    tw.append(list(sys.stdin.readline().rstrip()))
    for j in range(c):
        if tw[i][j] == "*":
            q.appendleft([0, i, j, "*"])
        elif tw[i][j] == "S":
            tmp.appendleft([0, i, j, "S"])
q.append(*tmp)  # 물의 좌표를 모두 넣어놓고 나중에 고슴도치 좌표를 넣기위해 함.
while q:
    day, x, y, hog_or_water = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if hog_or_water == "*" and (tw[nx][ny] == "." or tw[nx][ny] == "S"):
                tw[nx][ny] = "*"
                q.append([day + 1, nx, ny, hog_or_water])
            elif hog_or_water == "S" and tw[nx][ny] == ".":
                tw[nx][ny] = "S"
                q.append([day + 1, nx, ny, hog_or_water])
            elif hog_or_water == "S" and tw[nx][ny] == "D":
                print(day + 1)
                exit(0)
print('KAKTUS')
