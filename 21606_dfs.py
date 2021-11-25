import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def cal():
    count = 0
    visited = set()

    def dfs(exterior):
        cnt = 0
        for neighbor in graph[exterior]:
            if col[neighbor] == 1:
                cnt += 1
            else:
                if neighbor not in visited:
                    visited.add(neighbor)
                    cnt += dfs(neighbor)
        return cnt

    for i in range(1, numVertices + 1):
        # 각 실내별 인접한 실내 구하기
        if col[i] == 1:
            for j in graph[i]:
                if col[j] == 1:
                    count += 1
        # 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤
        # 각 덩어리별로 n*(n-1)의 경우의 수를 계산
        else:
            if i not in visited:
                visited.add(i)
                tmp = dfs(i)
                count += tmp * (tmp - 1)

    return count


numVertices = int(input())
col = list(map(int, list("0" + input().strip())))

graph = [[] for _ in range(numVertices + 1)]

for _ in range(1, numVertices):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(cal())



# # import sys
# #
# #
# # def dfs(x):
# #     global count
# #     visit[x] = 1
# #     for candy in graph[x]:
# #         if visit[candy] == 0:
# #             if go[candy] == 1:
# #                 visit[candy] = 1
# #                 count += 1
# #             else:
# #                 dfs(candy)
# #
# #
# # n = int(sys.stdin.readline())
# # graph = [[] * (n + 1) for _ in range(n + 1)]
# # go = [-1] + list(map(int, sys.stdin.readline().rstrip()))  # 실내/ 실외 저장 101010101010
# # out = []  # 실내 index 저장.(시작점 방지)
# # for _ in range(1, n):
# #     i, j = map(int, sys.stdin.readline().split())
# #     graph[i].append(j)
# #     graph[j].append(i)
# # for _ in range(n):
# #     if go[_] == 0:
# #         out.append(_)
# #
# # count = 0
# # for q in range(1, n + 1):
# #     visit = [0] * (n + 1)
# #     if q not in out:
# #         dfs(q)
# # print(count)

# import sys
#
# n = int(sys.stdin.readline())
# a = [0] + list(map(int, sys.stdin.readline().rstrip()))
# graph = [[] * (n + 1) for _ in range(n + 1)]
# # print(a)
# for _ in range(1, n):
#     i, j = map(int, sys.stdin.readline().split())
#     graph[i].append(j)
#     graph[j].append(i)
# count = 0
# out = []
# visited = [0] * (n + 1)
# # print(graph)
# # print(a)
# for i in range(1, n):
#     if a[i] == 0:
#         out.append(i)
#     if a[i] == 1:
#         for j in graph[i]:
#             # print("i=", i, "j=", j, a[i], a[j])
#             if visited[j] == 0:
#                 if a[j] == 1 and a[i] == 1:
#                     count += 1
#     visited[i] = 1
# # print(count)
# tmp_ = []
# for i in out:
#     tmp = 0
#     for j in graph[i]:
#         if j not in out:
#             tmp += 1
#     tmp_.append(tmp)
# # print(tmp_)
# for i in range(len(tmp_)):
#     zzz = tmp_[i]
#     if zzz != 1:
#         # print(zzz * (zzz - 1) // 2)
#         count += zzz * (zzz - 1) // 2
# print(2 * count)
#
# from sys import setrecursionlimit, stdin
#
# setrecursionlimit(10 ** 9)
# """문제 풀이 논리
# 1. 실외 점을 기준으로 인접해있는 실내 노드 개수를 count한다.
# 2. 실외 점을 중간에 놓고 실내 점 n개가 붙어있을 때 갈 수 있는 경로의 수는 n * 1(중간 실외 점 선택) * (n-1) = n*(n-1)에 해당.
# 3. 실외 노드끼리 연결되는 경우는 1) 실외끼리 인접 노드로 연결될 때 2) 중간에 실내 노드를 끼고 연결할 때. 이를 분리해서 생각.
# """
#
#
# def dfs(v, cnt):  # v: 정점 번호 & cnt: 실외와 연결된 실내 노드 개수 카운트
#
#     visited[v] = True
#
#     for i in graph[v]:  # 노드 v와 연결된 인접 노드를 하나씩 불러온다.
#         if location[i] == 1:  # 해당 노드의 위치가 실내이면
#             cnt += 1  # 실내 개수 카운트에 +1을 해준다
#         elif not visited[i] and location[i] == 0:  # 방문하지 않고 해당 i 점의 위치가 실외이면
#             cnt = dfs(i, cnt)  # 해당 실외 점을 기준으로 dfs를 돈다!
#
#     return cnt
#
#
# ans = 0
# n = int(stdin.readline())  # 정점 수 받기
#
# location = [0] + list(map(int, stdin.readline().strip()))  # location 정보 받아오기: 앞에 0 추가하는 이유는 노드의 인덱스 번호를 1부터 시작하기 위해
#
# graph = [[] for _ in range(n + 1)]  # 1번 노드부터 n번 노드까지 다 받아와야 하니
#
# for _ in range(n - 1):  # 셋째 줄부터 n+1번 줄까지 받기
#     a, b = map(int, stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
#     if location[a] == 1 and location[b] == 1:  # 둘다 실내이면
#         ans += 2  # 서로 방문하는 케이스가 2가지이니 이걸 정답에 함께 바로 세는 걸로.
#
# sum = 0
# visited = [False] * (n + 1)
# for i in range(1, n + 1):
#     if not visited[i] and location[i] == 0:  # 실외인 애들을 기준으로
#         x = dfs(i, 0)  # 현재 cnt = 0
#         sum += x * (x - 1)  # 실외인 노드를 기준으로 인접 노드 애들 개수 세는 게 총 n*(n-1)이니 실외 노드 걸릴 때마다 이걸 전부 세기
#
# print(sum + ans)