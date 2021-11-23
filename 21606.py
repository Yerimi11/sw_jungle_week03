import sys


def dfs(x):
    global count
    visit[x] = 1
    for candy in graph[x]:
        if visit[candy] == 0:
            if go[candy] == 1:
                visit[candy] = 1
                count += 1
            else:
                dfs(candy)


n = int(sys.stdin.readline())
graph = [[] * (n + 1) for _ in range(n + 1)]
go = [-1] + list(map(int, sys.stdin.readline().rstrip()))  # 실내/ 실외 저장 101010101010
out = []  # 실내 index 저장.(시작점 방지)
for _ in range(1, n):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
for _ in range(n):
    if go[_] == 0:
        out.append(_)

count = 0
for q in range(1, n + 1):
    visit = [0] * (n + 1)
    if q not in out:
        dfs(q)
print(count)
