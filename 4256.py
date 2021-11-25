import sys

sys.setrecursionlimit(10 ** 8)
m = int(sys.stdin.readline())


def postorder(start, end, dist):
    if dist == 1:
        anw[x].append(preorder_[start])
    else:
        root = preorder_[start]
        new_dist = 0
        for i in range(dist):
            if inorder[end + i] == root:
                break
            new_dist += 1
        if new_dist != 0:
            postorder(start + 1, end, new_dist)
        if dist - new_dist - 1 != 0:
            postorder(start + new_dist + 1, end + new_dist + 1, dist - new_dist - 1)
        anw[x].append(root)


anw = [[] for _ in range(m)]
for x in range(m):
    n = int(sys.stdin.readline())
    preorder_ = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))
    postorder(0, 0, n)

for _ in anw:
    print(*_)
