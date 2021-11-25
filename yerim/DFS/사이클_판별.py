#https://www.youtube.com/watch?v=aOhhNFTIeFI&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=8
# 서로소 집합 자료구조

# 특정 원소가 속한 집합을 찾기
from typing import ParamSpec


def fine_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = fine_parent(parent, parent[x]) # 경로 압축(부모 테이블 값 바로 갱신)
    return parent[x]                                # find호출 후 해당 노드의 루트노드가 바로 부모노드가 됨(15:30)

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = fine_parent(parent, a)
    b = fine_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
    
cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    #사이클이 발생한 경우 종료 # 부모노드가 같다면 같은 집합에 속해있다는 것 -> 사이클이 발생했다는 것.
    if fine_parent(parent, a) == fine_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(Union) 연산 수행
    else:
        union_parent(parent, a, b)
        
if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")