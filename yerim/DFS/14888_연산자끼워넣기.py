# from os import device_encoding
import sys
input = sys.stdin.readline

def cal(count, result, plus, minus, mulitiply, divide):
    if count == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    else:
        if plus:
            cal(count+1, result + nums[count], plus - 1, minus, mulitiply, divide)
        if minus:
            cal(count+1, result - nums[count], plus, minus - 1, mulitiply, divide)
        if mulitiply:
            cal(count+1, result * nums[count], plus, minus, mulitiply - 1, divide)
        if divide: # 추가해야할 조건) 음수를 양수로 나눌 땐 양수로 바꿔서 계산한 후 나온 몫을 음수로 바꾼다
            cal(count+1, result // nums[count], plus, minus, mulitiply, divide - 1)
        

        # +가 2개 올 수도 있는데? -> plus 라는게 들어오는지 확인하려면?
        

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split())) # 계산할 숫자
    calculate = list(map(int, input().split()))
    max_result = -1000000001
    min_result = 100000001
    # result = []
    
    def cal(1, nums, calculate[0], calculate[1], calculate[2], calculate[2])
    print(max(result))
    print(min(result))
