import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

Vn, En = map(int, input().split())

# 대소관계를 받아서 빈 리스트 V, U에 대소관계를 입력한다.
V = [[] for i in range(Vn + 1)]
U = [[] for i in range(Vn + 1)]
for i in range(En) : 
    big, small = map(int, input().split())
    V[big].append(small)
    U[small].append(big)

# now보다 작은 next가 아직 방문하지 않은 곳이라면, 재귀하는 함수
def DFSV(now) : 
    gone[now] = True
    for next in V[now] : 
        if not gone[next] : 
            DFSV(next)
# now보다 큰 next가 아직 방문하지 않은 곳이라면, 재귀하는 함수
def DFSU(now) : 
    gone[now] = True
    for next in U[now] : 
        if not gone[next] : 
            DFSU(next)
            
count = 0
#각각의 점 i에 대해 DFS들을 실행해준다
for i in range(1, Vn + 1) : 
    gone = [False for i in range(Vn + 1)]
    DFSV(i)
    if sum(gone) - 1 >= Vn // 2 + 1 : 
        count = count + 1
    # DFSV를 실행하면 gone이 차있으니 리셋하고 DFSU를 실행
    gone = [False for i in range(Vn + 1)]
    DFSU(i)
    if sum(gone) - 1 >= Vn // 2 + 1 : 
        count = count + 1
print(count)
