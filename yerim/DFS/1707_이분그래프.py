import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def DFS(v, group):
    visited[v] = group # 방문한 노드에 group 할당
    for i in graph[v]:
        if visited[i] == 0: # 아직 안 가본 곳이면 방문
            if not DFS(i, -group): # -값으로 DFS 실행해봄 -> 왜 -? 그룹 구분 1/2로 하는 것처럼 1/-1로함
                return False
        elif visited[i] == visited[v]: # 방문한 곳인데, 그룹이 동일하면 이분그래프가 아니니까 False
            return False    # v는 내가 방문하고있는 노드, i는 v의 인접리스트 안에 있는 노드
    return True
    

if __name__ == '__main__':
    k = int(input())
    for _ in range(k):
        v, e = map(int, input().split())
        graph = [[] for i in range(v+1)] # 빈 그래프 생성
        visited = [0] * (v+1) # 방문한 정점 체크
        
        for _ in range(e):
            a, b = map(int, input().split())
            graph[a].append(b) # 무방향 그래프
            graph[b].append(a) # 무방향 그래프
        
        bipatite = True # DFS 결과를 저장할 변수
        for i in range(1, v+1):
            if visited[i] == 0: # 방문한 정점이 아니면, dfs 수행
                bipatite = DFS(i, 1)
                if not bipatite:
                    break
    
        print('YES' if bipatite else 'NO')
    