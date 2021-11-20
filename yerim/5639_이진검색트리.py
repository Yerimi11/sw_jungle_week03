# # input file 기준 
# # 50 30 24 5 28 45 98 52 60 을
# # 5 28 24 45 30 60 52 98 50
import sys
sys.setrecursionlimit(100000) #재귀 반복횟수 늘림 (재귀 디폴트 1000개)
input = sys.stdin.readline
def getPostorder(nums):
    length = len(nums)
    # 입력받은 리스트의 길이가 1보다 작을 경우 리스트를 원본 그대로 반환
    if length <= 1:
        return nums
    # 루트 노드를 그대로 놔두려고 1부터 시작했나?
    for i in range(1, length):
        # 루트 노드(nums[0])보다 받은 값이 큰 경우 오른쪽 서브트리로 이동
        if nums[i] > nums[0]:
            # 왼쪽 서브트리 + 오른쪽 서브트리 + 루트 
            # 큰수 비교하는 동시에 서브트리를 후위 순회로 바꿔줌
            return getPostorder(nums[1:i]) + getPostorder(nums[i:]) + [nums[0]]
    # 맨 마지막 작업. 후위 순회는 루트 노드가 맨 마지막에 오니까 순서바꾸기
    return getPostorder(nums[1:]) + [nums[0]] #최종 후위 순회~
if __name__ == '__main__':
    nums = []
    while True:
        try:
            nums.append(int(input()))
        except:
            break
    # 재귀 최종 리턴 받은 값들 후위 순회로 받음
    nums = getPostorder(nums)
    for n in nums:
        print(n)