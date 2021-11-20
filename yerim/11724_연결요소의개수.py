import sys
input = sys.stdin.readline

N, M = map(int, input().split())
V = {}
for i in range(1, N + 1) : 
    V[i] = [] # 빈 리스트 채워줌 V: {1: [], 2: [], ...}
for i in range(M) : 
    v1, v2 = map(int, input().split()) # 입력받는 행, 렬 1 2 일때 v1:1, v2:2 
    V[v1].append(v2) # V의 ┌ v1(1)번째자리에 v2(2)가 들어감
    V[v2].append(v1) # V: {1: [2], 2: [1], 3:[]...} => 1번 노드는 2번 노드랑 연결되어있고..
    # 반대로 넣는 이유? 어느 노드랑 서로 연결되어있는지 체크하려고
# print(V)
gone = [] # BFS가 실행될 때 gone을 다시 비워줌. 
count = 0
def BFS(now) : 
    que = [now] # 큐를 만들고 큐에 나우 하나만 넣음
    while que : # 큐라는 리스트에 아직 안 간 곳이 추가 됨
        q = que[0]
        gone.append(q) #방문했다고 체크 // 해당 노드 경로 봤으니 봤다고 넣어주고
        del que[0] #체크했으니 지움
        for i in V[q] : # V: {1: [2,5], 2: [1,5], 3:[4], 4:[3,6],..}
            if not i in gone and not i in que : # 이미 간 곳도 아니고 갈 예정도 아닐 때
                que.append(i) # que:[] -> que: [2,3,4]
                #que에 넣어서 i랑 연결된 노드들도 확인하게 함
                
for i in range(1, N + 1) : 
    if not i in gone : # 간 곳 중에 하나가 아니면 
        count = count + 1 # 연결된 별개가 하나 더 있는거니까 셈
        BFS(i) # 정점의 갯수 n만큼 BFS 반복
print(count)