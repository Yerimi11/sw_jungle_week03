import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
check = [[-1]*n for i in range(n)]
for i in range(n):
    temp = list(sys.stdin.readline().strip())
    graph[i] = list(map(int, temp)) # 간선들의 정보가 들어있는 (인접)리스트

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs():
    q = deque()
    q.append([0,0])
    check[0][0] = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if check[nx][ny] == -1:
                    if graph[nx][ny] == 0:
                        check[nx][ny] = check[x][y] + 1 # check : 벽 뿌순 횟수
                        q.append([nx,ny])
                    else:
                        check[nx][ny] = check[x][y]
                        q.appendleft([nx, ny])

bfs()
print(check[n-1][n-1])