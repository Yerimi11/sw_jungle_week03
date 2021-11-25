# import sys

# v, e = map(int, sys.stdin.readline().split())
# a, b, c = list(map(int, sys.stdin.readline().split()))

# 크루스칼 알고리즘
# 유니온 파인드 (합집합 찾기)

from sys import stdin
input = stdin.readline
# V:노드의 갯수, E:간선의 갯수
V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key=lambda x: x[2]) # 가중치값을 기준으로 (배열)정렬해준다(유니온파인드 핵심)

ans = 0 # 우리가 찾으려는 가중치의 최솟값. 초기값 세팅
parent = [i for i in range(V+1)] # 부모노드 임의로 01234식으로 배열을 주고 찾음 0부터 v까지
        # ㄴ여기 왜 i지?? -> i를 v번 반복해서 써줌 => [0, 1, 2, 3]
def find(a):                        # 원래 부모노드값 초기값은 위에 ┌ 배열 [0, 1, 2, 3] 니까.
    if a != parent[a]: # 1이 들어오면 1의 부모값과 비교하고 둘이 같지 않으면 뭔가 경로가 바꼈다는 뜻. 
        parent[a] = find(parent[a])  # 같지않으면 부모 노드의 바뀐 값을 넣어서 한 번 더 찾아줌 (부모값바꿈)
    return parent[a] # 그게 아니면 일반적인 자기 부모 값을 반환한다

def union(a, b): # 1번노드와 2번노드의 부모값이 들어옴
    a,b = find(a),find(b) # 1번노드와 2번노드의 부모값을 찾음
    # 2번노드의 부모값과 1번노드의 부모값을 바꿔버림. 둘이 이어졌다하면 루트노드를 바꿔야 이어졌다고 보니까
for i in graph:
    a, b, c = i             # 부모노드값이 같은지 확인하는거임. 그래서 다르면 연결시킴(union)
    if find(a) != find(b): # 싸이클인지 아닌지 확인하는 구문 # 1번 2번 꺼내서 비교해보고..
        union(a,b) # 둘이 같지않으면 떨어져있다고 가정하고 합쳐버림 (부모노드 연결)
        ans +=c #가중치 합함 # 0번은 맞춰주려 넣은거니 무시해도 됨
    #만약 a b c 값을 받았는데 노드 둘을 이었을 때 사이클이 된다면 스킵해버림(else) (최소신장트리는 사이클이 없어야해서)
        
print(ans)

# 7:25 // 25line 설명 // 2번노드의 부모값과 1번노드의 부모값을 바꿔버림. 둘이 이어졌다하면 루트노드를 바꿔야 이어졌다고 보니까
# union -> 1번 2번 꺼냄 비교. 경로는 모르지만 가중치는 아니까 1번노드의 부모값을 찾음
# 0번은 맞춰주려고 넣으니 무시, 그럼 find(a)는 find(1)이고, find(b)는 find(2)
# 20번째줄로 가서 a는 1, 부모노드의 1번 인덱스도 1 ([0,1,2,3,4])이니까 부모노드값 리턴 (1 리턴)
# find(b)도 2 넣었을 때 그대로 부모노드값 리턴2 (26line복귀)(리턴값이 나오면 둘이 이어져있지 않다는 것)
# 만약 20번째줄에서 둘이 같지 않으면 둘이 이어 (25->29line으로 내려감)> union 사용 >가중치 합

# # 1197 - 주석 없는 ver.
# import sys
# input = sys.stdin.readline

# v, e = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(e)]
# graph.sort(key=lambda x: x[2])

# ans = 0
# parent = [i for i in range(v+1)]

# def find(a):
#     if a != parent[a]:
#         parent[a] = find(parent[a])
#     return parent[a]

# def union(a, b):
#     a,b = find(a), find(b)
    
# for i in graph:
#     a, b, c = i
#     if find(a) != find(b):
#         union(a,b)
#         ans += c
        
# print(ans)