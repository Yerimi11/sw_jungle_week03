import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
# 4방향 탐색
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 보드에 입력받음
board = [list(map(int, input().split())) for _ in range(n)]
# 배열 / 0으로 다 초기화
dis = [[0]*n for _ in range(n)]
Q=deque()
Q.append((0, 0)) # 출발점 좌표
board[0][0]=1 # 한 번 방문한 곳은 1로 체크해서 벽으로 만듦. 이동 못하게

while Q: # Q가 비어있으면 거짓이 돼서 멈추도록
    tmp=Q.popleft # 첫 좌표(0,0)이 빠짐
    for i in range(4): # 4방향 탐색
        x = tmp[0]+dx[i] # x좌표 0, 방향전환 12시방향
        y = tmp[1]+dy[i] # 3시 방향
        # x값이 이 범위 안에 있어야 경계선 밖으로 나가지 않음 6->n-1, board : 벽이면 가지 않도록. 1이면 벽, 0은 통로
        if 0<=x<=(n-1) and 0<=y<=(n-1) and board[x][y]==0:
            board[x][y]=1 # 1로 체크해서 벽으로 만들어버림. 다시는 못가게
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y)) # Q가 돌도록 함. 끝

if dis[(n-1)][(n-1)]==0: 
    print(-1) # 답이 아니면 -1 출력
else:
    print(dis[(n-1)][(n-1)]) # 답 출력
