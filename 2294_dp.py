import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
dp = [999999999] * (k + 1)
dp[0] = 0
for _ in range(n):
    lst.append(int(input()))

lst.sort()
for price in lst:
    for i in range(price, k + 1):
        dp[i] = min(dp[i - price] + 1, dp[i])
    # print(dp)
print(dp[-1] if dp[-1] != 999999999 else -1)

#
# import sys
#
#
# # 제일 큰거로 넣어보면서 해보고싶음.
# # 최대힙? 우선순위큐?
#
# def min_coin_count(value, coin_list):
#     # 누적 동전 개수
#     count = 0
#     coin_list.sort(reverse=True)
#
#     # coin_list의 값들을 큰 순서대로 본다
#     for i in coin_list:
#         # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인한다
#         count += (value // i)
#         if value == i:
#             return count + 1
#         value -= (value // i) * i
#     if value != 0:
#         return -1
#     return count
#
#
# n, k = map(int, sys.stdin.readline().split())
# money = sorted(list(int(sys.stdin.readline().rstrip()) for _ in range(n)))
# # while k < money[-1]:
# #     del money[-1]
# if k == money[-1]:
#     print(1)
#     exit(0)
# elif k % money[-1] == 0:
#     print(k // money[-1])
#     exit(0)
# anw = [sys.maxsize]
# while money:
#     if k // money[-1] < min(anw):
#         anw.append(min_coin_count(k, money))
#     del money[0]
# # print(anw)
# print(min(anw))
