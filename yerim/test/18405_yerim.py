import sys
input = sys.stdin.readline
from collections import deque

# n, k = map(int, input().split())
# need_visit = []
# checklist = [[[False for i in range(n)] for j in range(k)]]
# graph = [[] for _ in range(k+1)]
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     graph[a].append(b)

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def BFS(graph, start_node): # 그래프와 시작 Node를 넣음
#     queue = deque()
#     # start_node를 맨 처음 방문 대기열에 추가
#     need_visit.append(start_node)
#     # 방문 대기열이 존재하지 않을 때 까지 반복
#     while need_visit:
#         node = need_visit.pop(0) # 대기열에서 맨 처음 요소를 제거하고 node에 담음
#         if node not in checklist: # node가 방문 완료 queue에 있는지 확인
#             checklist.append(node) # 없으면 방문 완료 queue에 추가
#             need_visit.extend(graph[node]) # node와 연결된 Node들을 대기열에 추가
#     return checklist 
# # BFS TEST
# print(BFS(graph, 'A')) # ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']


#     a, b, c = queue.popleft()
#     for i in range(4) : 
#         x = a + dx[i]
#         y = b + dy[i]
#         if 0 <= x < n and 0 <= y < k == False : 
#             checklist[y][x] = True
#             need_visit[y][x] = need_visit[b][a] + 1
#             queue.append([x, y])

# f = True
# date = 0
# for j in range(k) : 
#     for i in range(n) : 
#         if need_visit[j][i] == 0 : 
#             f = False
#         date = max(date, need_visit[j][i] - 1)
# if f : 
#     print(date)
# else : 
#     print(0)



###

# n개의 줄과 원소, k 이하의 바이러스 번호
n, k = map(int, input().split())
virus = []
graph = []
for x in range(n): # 2차원 리스트 받기
    graph.append(list(map(int, input().split())))
    for y in range(n):
        # graph에서 virus 정보 받아오기
        if graph[x][y] != 0:
            virus.append(((graph[x][y], x, y))) # 바이러스 번호, 좌표
                    # (x,y)자리에 있는 virus 번호 저장

# 2차원 리스트 받기(토마토)
# for j in range(m) : 
#         B[k].append(list(map(int, input().split())))
#         for i in range(n) : 
            # tomato = B[k][j][i]
            # if tomato == 1 : 
            #     que.append([i, j])


seconds, x, y = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def BFS(seconds, x, y):
    # global time_count
    time_count = 0
    q = deque(virus) #q에 바이러스 정보 넣음
    while q:
        if time_count == seconds: 
            break

        for _ in range(len(q)):
            virusnum, x, y = q.popleft() # 한 줄 빼서 탐색
            for i in range(4): # 동서남북 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0: # 동서남북 중 이동할 좌표 값이 0이면
                        graph[nx][ny] = graph[x][y] # 현재 바이러스 번호를 이동할 좌표에 퍼뜨림
                        q.append((graph[nx][ny], nx, ny)) # 바뀐 바이러스 좌표 정보 업데이트
                                # 현재 바이러스 번호, xy 좌표
            time_count += 1 # 초 카운팅
            return graph[x-1][y-1] # 동서남북 탐색 끝 원점으로 돌아옴
                        
virus.sort()
BFS(seconds, x, y)
# print(graph(seconds, x, y))
print(BFS(seconds, x, y)) # 초 카운팅 or BFS 시작점 잘못해서 0초가 출력되는 중,,


