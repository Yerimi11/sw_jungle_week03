import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
Tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    Tree[a].append(b) # tree의 a번째 인덱스에 b값을 넣는다
    Tree[b].append(a) # 반대로도 넣음
    
def DFS(start, tree, parents):
    for i in tree[start]: # 무슨 원리로 부모노드가 뽑히는거지?? - 인접노드
        if parents[i] == 0: 
            parents[i] = start # parents 에 [0,0,0..] 중에 i번째를 1로 바꿔준다(방문한 노드 1로)
            DFS(i, tree, parents)
            
DFS(1, Tree, parents)

for i in range(2, n+1):
    print(parents[i])