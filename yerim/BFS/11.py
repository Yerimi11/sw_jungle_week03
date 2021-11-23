import sys
from collections import deque

row, column = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(row)]

water = [[0] * column for _ in range(row)]
ddabong = [[0] * column for _ in range(row)]
destination = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q_water = deque()
q_ddabong = deque()

for i in range(row):
    for j in range(column):
        if arr[i][j] == 'S':
            q_ddabong.append([i,j])
            ddabong[i][j] = 1
        elif arr[i][j] == '*':
            q_water.append([i,j])
            water[i][j] = 1
        elif arr[i][j] == 'D':
            destination = [i,j]

water[destination[0]][destination[1]] = float('inf')

while q_water:
    x, y = q_water.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < row and 0<= ny < column and water[nx][ny] == 0 and arr[nx][ny] != 'X' and arr[nx][ny] != 'D':
            water[nx][ny] = water[x][y] +1
            q_water.append([nx,ny])
for i in water:
    print(i)


while q_ddabong:
    x, y = q_ddabong.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < row and 0<= ny < column and ddabong[nx][ny] == 0 and arr[nx][ny] != 'X':
            # if water[nx][ny] > ddabong[x][y] or [nx, ny] == destination:
            # if (ddabong[x][y] + 1 != water[nx][ny]) and (ddabong[x][y] < water[nx][ny]):
            if ddabong[x][y] + 1 < water[nx][ny] or water[nx][ny] == 0:
                ddabong[nx][ny] = ddabong[x][y] +1
                q_ddabong.append([nx,ny])
for i in ddabong:
    print(i)

# for i in range(row):
#     for j in range(column):
# print(destination)
# print(water[destination[0]][destination[1]])

time =ddabong[destination[0]][destination[1]] - 1

if time == -1:
    print('KAKTUS')
else:
    print(time)