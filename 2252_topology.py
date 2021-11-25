import sys
# 덱쓰면 이상한 오류뜸.
n, m = map(int, sys.stdin.readline().split())

# in_degree 저장할 리스트, 위상?이 0 인 애들을 먼저 빼내서,  출력하고 전체에 대해 -1, 또 뺴주고 출력 반복!

degree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]


for _ in range(1, m + 1):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    degree[j] += 1
    #  i 행에 j 저장.
    # 1 3
    # 1 2
    # graph[1] = [2, 3]
    # 1 -> 2, 1 -> 3 이런뜻임.
    # 3과 2는 위상이 높으므로 맨첨에 못빼준다.
    # 1이랑 화살표 삭제하면 2, 3이 남고, 위상 - 1 을 해준다.

# q 는 레벨이 낮은 애들부터 더해주고 빼는 기능을 할 리스트.
# answer 는 나중에 출력을 위해 낮은 위상인 애들 순으로 append 시켜줄 리스트임.
q = []
anw = []
print(degree)
for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)
# 저장된 degree 를 돌면서 위상이 0 인, 즉, 나를 모시는 애들이 없는 노드들을 탐색하여 q 에 저장해준다.
# q 에는 가장 먼저 출력될 친구들이 쌓임.
while q:
    for _ in q:
        # 제거후 answer 에 차곡차곡 순서대로 넣는다.
        # 인덱스로 접근한 것이 아니라서, 새롭게 인덱싱을 해줄 필요가 없다.
        q.remove(_)
        anw.append(_)
        for j in graph[_]:
            degree[j] -= 1
            print(degree)
            if degree[j] == 0:
                q.append(j)

print(*anw)
print(graph)
