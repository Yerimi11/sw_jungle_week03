import sys


def bfs(x):
    check = [None] * (V + 1)
    check[x] = True
    flag = True
    for k in range(1, V + 1):
        if not flag:
            break
        # for h in range(1, V + 1):
        # print(graph2)
        if graph2[k]:
            for neighbor in graph2[k]:
                # print(f'neighbor: {neighbor}')
                # if graph[h][k] == 1:
                if check[neighbor] is None:
                    check[neighbor] = False if check[k] else True
                else:
                    if check[k] == check[neighbor]:
                        print("NO")
                        flag = False
                        break
    # print(check)
    if flag:
        print("YES")


for _ in range(int(sys.stdin.readline())):
    V, E = map(int, sys.stdin.readline().split())
    # graph = [[0] * (V + 1) for _ in range(V + 1)]
    graph2 = [[] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        i, j = map(int, sys.stdin.readline().split())
        # graph[i][j] = graph[j][i] = 1
        if i != j:
            graph2[i].append(j)
            graph2[j].append(i)
    if V == 1:
        print("YES")
        continue
    count = 0
    for i in range(1, V + 1):
        if graph2[i]:
            bfs(i)
            break
        count += 1
    if count == V:
        print("YES")
