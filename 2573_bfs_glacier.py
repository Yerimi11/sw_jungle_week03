# import sys
#
#
# def bfs(lst):
#
#
# n, m = map(int, sys.stdin.readline().split())
# graph = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
# visit = list([0] * m for _ in range(n))
#
# for i in range(1, n):
#     if i == 1 or i == n - 1:
#         print()
#
# print(n, m)
# print(graph)
# print(visit)

# import sys
# from collections import deque
#
#
# def bfs(i, j, visit):
#     que = deque([[i, j]])
#     melting_que = deque()  # 빙하가 녹는 위치와 녹는 정도를 저장하는 큐
#     visit[i][j] = 1
#     while que:
#         i, j = que.popleft()
#         melt_cnt = 0
#         for d_x, d_y in direction:
#             next_x = i + d_x
#             next_y = j + d_y
#             if x - 1 >= next_x >= 0 == visit[next_x][next_y] and 0 <= next_y <= y - 1:
#                 # 빙산의 높이가 있고 방문을 안했을 경우 que 에 값 넣어주기
#                 if glacier[next_x][next_y] != 0:
#                     visit[next_x][next_y] = 1  # 방문 체크
#                     que.append([next_x, next_y])
#                 # 사방향 탐색 시 0일 경우 melt_cnt 증가
#                 else:
#                     melt_cnt += 1
#         if melt_cnt:
#             melting_que.append([i, j, melt_cnt])
#     return melting_que
#
#
# input = sys.stdin.readline
# year = 0  # 몇 년이 지났는지 판단하는 변수
# x, y = map(int, input().split())
# glacier = [[int(n) for n in input().split()] for _ in range(x)]
# direction = ((1, 0), (-1, 0), (0, -1), (0, 1))  # 동서남북
# # 반복문 종료 조건 -> 빙산의 갯수가 0이거나 2일 경우
# while True:
#     cnt = 0  # 빙산의 갯수를 담는 cnt 변수
#     visit = [[0 for _ in range(y)] for _ in range(x)]  # bfs를 위한 탐색 확인 리스트
#     for i in range(x - 1):
#         for j in range(y - 1):
#             if glacier[i][j] != 0 and visit[i][j] == 0:  # 빙하의 높이가 남아있고 방문하지 않을 경우
#                 cnt += 1  # 빙산의 갯수 추가
#                 melt = bfs(i, j, visit)  # bfs 시작을 하고 각 좌표별로 녹는 정도 반환
#                 while melt:
#                     m_x, m_y, m = melt.popleft()
#                     glacier[m_x][m_y] = max(glacier[m_x][m_y] - m, 0)
#     if cnt == 0:
#         year = 0
#         break
#     if cnt >= 2:
#         break
#     year += 1  # 일 년 증가
#     # 빙산의 갯수가 0이거나 2일 경우 반복문 종료
# print(year)

# N, M = map(int, input().split())
#
# board = []
#
# all_element = 0
#
# for _ in range(N):
#     board.append(list(map(int, input().split())))
#     all_element += M - board[-1].count(0)
#
# dy = (1, -1, 0, 0)
# dx = (0, 0, 1, -1)
#
#
# def find_start_point():
#     for y in range(N):
#         for x in range(M):
#             if board[y][x] != 0:
#                 return (y, x)
#     return (0, 0)
#
#
# start_point = find_start_point()  # 아무 점이나 찾아준다.
#
# will_remove = []
# stack = []
#
# t = 0
# sign = 1
#
# # 하루가 지남에 따라 while loop 한바퀴 돔
# while True:
#     sign *= -1
#     t += 1
#     count = 0
#     board[start_point[0]][start_point[1]] *= -1
#     stack.append(start_point)
#     while stack:
#         y, x = stack.pop()
#         count += 1
#         value = 0
#         for d in range(4):
#             if 0 <= y + dy[d] < N and 0 <= x + dx[d] < M:
#                 if board[y + dy[d]][x + dx[d]] == 0:
#                     value += 1
#                 elif board[y + dy[d]][x + dx[d]] * sign < 0:
#                     board[y + dy[d]][x + dx[d]] *= -1
#                     stack.append((y + dy[d], x + dx[d]))
#
#         if board[y][x] * sign - value <= 0:
#             will_remove.append((y, x))
#         else:
#             board[y][x] -= value * sign
#             start_point = (y, x)
#
#     # 덩어리가 2개 이상인 경우
#     if count != all_element:
#         print(t - 1)
#         break
#
#     # 제거될 친구들 제거
#     while will_remove:
#         y, x = will_remove.pop()
#         board[y][x] = 0
#         all_element -= 1
#
#     # 언제나 한덩이인 채로 모두 녹았을 경우
#     if all_element == 0:
#         print(0)
#         break


import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
T = []
que = deque()
for i in range(n):
    T.append(list(map(int, input().split())) + [None])
    for j in range(m):
        if T[i][j] != 0:
            que.append([i, j])
T.append([None for i in range(m + 1)])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def cutcheck(ice):
    gone = {}
    for a, b in ice:
        gone[(a, b)] = False
    a, b = ice[0][0], ice[0][1]
    gone[(a, b)] = True
    q = deque()
    q.append([a, b])
    check = 1
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if T[x][y] > 0 and not gone[(x, y)]:
                gone[(x, y)] = True
                q.append([x, y])
                check = check + 1
    if check != len(ice):
        return True
    return False


year = -1
que.append(['year', year - 1])
while que:
    a, b = que.popleft()
    if a != 'year':
        count = 0
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if year < T[x][y] <= 0:
                count = count + 1
        if T[a][b] > count:
            que.append([a, b])
            T[a][b] = T[a][b] - count
        else:
            T[a][b] = year
    else:
        if len(que) == 0:
            print(0)
            exit(0)
        else:
            if cutcheck(que):
                print(-year)
                exit(0)
            else:
                year = b
                que.append(['year', b - 1])
