import sys

n = int(sys.stdin.readline())
dic = {}
for i in range(n):
    root, left, right = sys.stdin.readline().split()
    dic[root] = [left, right]
print(dic)


def preorder(x):
    print(x, end="")
    if dic[x][0] != ".":
        preorder(dic[x][0])
    if dic[x][1] != ".":
        preorder(dic[x][1])


def inorder(x):
    if dic[x][0] != ".":
        inorder(dic[x][0])
    print(x, end="")
    if dic[x][1] != ".":
        inorder(dic[x][1])


def postorder(x):
    if dic[x][0] != ".":
        postorder(dic[x][0])
    if dic[x][1] != ".":
        postorder(dic[x][1])
    print(x, end="")


preorder('A')
print()
inorder('A')
print()
postorder('A')
