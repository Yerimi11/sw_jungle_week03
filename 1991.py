n = int(input())
dic = {}
for i in range(n):
    x, y1, y2 = input().split()
    dic[x] = [y1, y2]


def preorder(x):
    print(x, end='')
    if dic[x][0] != '.':
        preorder(dic[x][0])
    if dic[x][1] != '.':
        preorder(dic[x][1])


def inorder(x):
    if dic[x][0] != '.':
        inorder(dic[x][0])
    print(x, end='')
    if dic[x][1] != '.':
        inorder(dic[x][1])


def postorder(x):
    if dic[x][0] != '.':
        postorder(dic[x][0])
    if dic[x][1] != '.':
        postorder(dic[x][1])
    print(x, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')


#
# import sys
#
# input = sys.stdin.readline
#
#
# class Node:  # 바이너리 트리를 구성 할 노드 클래스 생성
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def preorder(node):  # 전위 순회
#     print(node.data, end='')
#     if node.left != '': preorder(node.left)
#     if node.right != '': preorder(node.right)
#
#
# def inorder(node):  # 중위 순회
#     if node.left != '': inorder(node.left)
#     print(node.data, end='')
#     if node.right != '': inorder(node.right)
#
#
# def postorder(node):  # 후위 순회
#     if node.left != '': postorder(node.left)
#     if node.right != '': postorder(node.right)
#     print(node.data, end='')
#
#
# n = int(input())
# tree_li = []
# for i in range(n):
#     data = input().split()
#     node = Node(data[0])  # 부모 노드는 데이터로 저장하여 클래스 생성
#
#     # 자식 노드들 중 . 으로 입력된 데이터는 공백으로 처리
#     if data[1] == '.': data[1] = ''
#     if data[2] == '.': data[2] = ''
#
#     # 자식 노드 저장
#     node.left = data[1]
#     node.right = data[2]
#
#     # 노드 클래스들을 트리 리스트에 추가
#     tree_li.append(node)
#
# for i in range(n):
#     for j in range(n):
#         # 트리 리스트들의 부모 노드와 자식 노드들을 서로 매칭시켜 트리 구성
#         if tree_li[i].data == tree_li[j].left:
#             tree_li[j].left = tree_li[i]
#         elif tree_li[i].data == tree_li[j].right:
#             tree_li[j].right = tree_li[i]
#
# preorder(tree_li[0])
# print()
# inorder(tree_li[0])
# print()
# postorder(tree_li[0])
