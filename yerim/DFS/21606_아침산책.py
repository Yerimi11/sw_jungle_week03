import sys 
from collections import defaultdict
# 실외로 연결된 실내의 경로를 서치하는 함수
# 현재 노드에서 시작해서 만들 수 있는 모든 경로의 수를 return
def dfs(graph, node, inout, count=0):
    if inout[node] == 1: # 실내로 들어갔을 때 경로 +1 하고 끝냄
        return count + 1 
    
    inout[node] = 2 # 실외이면서 방문한 노드라면 2로 변경
    for next_node in graph[node]:
        if inout[next_node] == 2: # 방문을 했고 실외이면 패스
            continue
        count = dfs(graph, next_node, inout, count)
    return count 

# 실외로 연결된 실내의 경로의 수를 세는 함수
def count_path(n, graph, inout):
    count = 0
    for start_node in range(1, n+1):
        if inout[start_node] == 0:  # 현재 방문한 노드가 실외이면
            outdoors = dfs(graph, start_node, inout)     
            count += outdoors * (outdoors-1)
    # # 실내-실내 셈
    # for start_node in range(1, n+1):
    #     if inout[start_node] == 1:
    #         inout[start_node] = 0
    #         outdoors = dfs(graph, start_node, inout) 
    #         inout[start_node] = 1    
    #         count += outdoors
    return count

if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    input = sys.stdin.readline
    n = int(input())    # 정점의 개수
    inout = list(map(int, '0' + input().rstrip()))  # 0번째 인덱스 무시하려고 넣은 값
    
    graph = defaultdict(list)
    incount = 0
    for _ in range(n-1):
        src, dst = map(int, input().split()) # src:source, dst:destination

        # 둘 다 실내일 때 (수정코드)
        if inout[src] == inout[dst] == 1:
            incount += 2
            continue
        else:
            graph[src].append(dst)
            graph[dst].append(src)
        # 여기까지
    print(incount + count_path(n, graph, inout))