# 골드 4레벨        최소 스패닝 트리
# 크루스칼 알고리즘
# 유니온 파인드
from sys import stdin

read = stdin.readline
V, S = map(int, read().split())

edge = []
for _ in range(S):
    a, b, w = map(int, read().split())
    edge.append((w, a, b))
edge.sort(key=lambda x: x[0])
parent = list(range(V + 1))


# range 1~ 안댐


def connect(a, b):
    a = check(a)
    b = check(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a


def check(a):
    if a == parent[a]:
        return a
    parent[a] = check(parent[a])  # 경로 압축
    return parent[a]  # check(parent[a])


sum = 0
for w, s, e in edge:
    if check(s) != check(e):
        connect(s, e)
        sum += w

print(sum)
