import sys

def DFS1(node): #전위 preorder
    if node == '.':
        return
    else:
        print(node,end='')
        DFS1(tree[node][0])
        DFS1(tree[node][1])
        
def DFS2(node): #중위 inorder
    if node == '.':
        return
    else:
        DFS2(tree[node][0])
        print(node,end='')
        DFS2(tree[node][1])
        
def DFS3(node): #후위 postorder
    if node == '.':
        return
    else:
        DFS3(tree[node][0])
        DFS3(tree[node][1])
        print(node,end='')
                

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tree = {}
    
    for _ in range(n):
        root, left, right = map(str, sys.stdin.readline().split())
        tree[root] = [left, right]
    
    DFS1('A')
    print()
    DFS2('A')
    print()
    DFS3('A')
