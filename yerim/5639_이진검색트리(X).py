# import sys
        
#     #전위를 반대로 써서 받아보면? 입력 받는 값은 이거의 반대로 / 반대면 후위인가
    
# def DFS3(node, temp): #후위
#     if node == '.':
#         return
#     else:
#         DFS3(tree, temp)
#         DFS3(tree, temp)
#         temp = node #temp에 거꾸로 저장해두기
        
        
# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#     tree = {}
#     temp = []
    
#     for _ in range(n):
#         tree = list(sys.stdin.readline().split())
#     # for _ in range(n):
#     #     root, left, right = map(str, sys.stdin.readline().split())
#     #     tree[root] = [left, right]
    
#     DFS1('A', temp)



import sys
sys.setrecursionlimit(10**9)
preorder = []

while True:
    try: #데이터가 몇 개가 들어올지 모를 때 (일단 해보자) try-except
        preorder.append(int(sys.stdin.readline()))
    except: #일단 해보다가 뭔가 오류가 생겼을 때
        break #이거때매 엔터 두번 쳐야 입력됨 (엔터가 있어야 예외로 쳐서)
postorder = []

def postorderset(preorder, start, end):
    if start > end:
        return
    root = preorder[start]
    ls = start + 1
    re = end
    rs = end + 1
    
    for i in range(end-start+1):
        if i == 0:
            continue
        if preorder[start+i] > root: # 루트보다 큰 수 찾기
            rs = i + start # 루트보다 첫번째로 커지는 수를 오른쪽 프리오더의 시작으로 정함
            break
    le = rs - 1
    # 후위 만들기
    postorderset(preorder, ls, le) #왼쪽 프리오더 순환
    postorderset(preorder, rs, re) #오른쪽 프리오더 순환
    postorder.append(root) #후위 순회 : 왼+오+루트 마지막에 합침
    
postorderset(preorder, 0, len(preorder) -1)
for i in postorder:
    print(i)