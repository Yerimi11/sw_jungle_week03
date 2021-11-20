import sys


sys.setrecursionlimit(10 ** 6)

preorder = []


def postorder(start, end):
    if start >= end:
        return
    root = preorder[start]

    if preorder[end - 1] <= root:
        postorder(start + 1, end)
        print(root)
        return

    for i in range(start + 1, end):
        if preorder[i] > root:
            idx = i
            break
    postorder(start + 1, idx)
    postorder(idx, end)
    print(root)


while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

postorder(0, len(preorder))
