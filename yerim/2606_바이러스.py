import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
V = {}
for i in range(1, N + 1) : 
    V[i] = []
for i in range(M) : 
    v1, v2 = map(int, input().split())
    V[v1].append(v2) # V의 ┌ v1(1)번째자리에 v2(2)가 들어감
    V[v2].append(v1) # V: {1: [2], 2: [1], 3:[]...} => 1번 노드는 2번 노드랑 연결되어있고..
    # 반대로 넣는 이유? 어느 노드랑 서로 연결되어있는지 체크하려고
for i in range(1, N + 1) : 
    V[i].sort()
# print(V) # {1: [2, 5], 2: [1, 3, 5], 3: [2], 4: [7], 5: [1, 2, 6], 6: [5], 7: [4]}

gone = []
count = 0
def BFS(now) : 
    global count
    que = [now]
    while que : 
        q = que[0]
        gone.append(q) # 해당 노드 경로 봤으니 봤다고 넣어주고
        del que[0]
        for i in V[q] : # {1: [2, 5], 2: [1, 3, 5] 에서 봄
            if not i in gone and not i in que : 
                que.append(i) #que에 넣어서 i랑 연결된 노드들도 확인하게 함
                count = count + 1 #부모노드랑 연결된 자식노드들 연결됐는지 보고 하나 카운팅 
                # (BFS니까 순서대로 갈 때마다 1이랑 연결된거니 카운팅)
BFS(1)
print(count)