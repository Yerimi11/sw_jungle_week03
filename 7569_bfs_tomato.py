# M * N * H 토마토

# 격자모양 상자의 칸에 하나씩, 수직으로 쌓아올려서 창고에 보관.

# 익은토마토, 익지 않은 토마토

# 하루 지나면 익은토마토가 안익은 토마토 전염. <- why? (동서남북 + 상자 윗칸, 아래칸)

# 혼자는 토마토가 안익음  <- why?

# 상자의 토마토가 며칠만에 익는지 최소 일수 출력.

# M 가로, N 세로, H 높이  2 <= M,N <= 100, 1<= H <= 100
#  1 : 익토, 0 : 안익토, -1 : empty
#  x, y, z 축 으로 조지기.
#  일단 큐를 만든다.
#  큐에 익어있는 토마토들의 좌표를 모두 append 해준다.
#  덱에 넣어 놓았던 좌표들을 하나씩 꺼내면서 동서남북 상하를 돌며 0인 곳에 전에 있던 곳 + 1로 저장한다.
#  0일차 일 때, 1 이므로 1일차에 익은 토마토들이 0 -> 2 가돼서 마지막에 -1 해줘야댐.
#  새롭게 익은 토마토들을 큐에 추가해준다.
import sys
from collections import deque


def tomato_ghost():
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 1 <= nz < h + 1:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    q.append((nz, nx, ny))
        # print(box)


m, n, h = map(int, sys.stdin.readline().split())
box = dict()
day = 0
for _ in range(1, h + 1):
    box[_] = []
    for __ in range(n):
        box[_].append(list(map(int, sys.stdin.readline().split())))

q = deque()
for i in range(1, h + 1):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i, j, k))
tomato_ghost()
tmp = - sys.maxsize
for i in range(1, h + 1):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            tmp = max(tmp, box[i][j][k])

print(tmp - 1)
