# 실패

# import copy
# import sys
# input = sys.stdin.readline
#
# N = int(input().strip())
# rgb_list = []
#
# for _ in range(N):
#     rgb_list.append(list(map(int, input().strip().split())))
#
# R = 0
# G = 1
# B = 2
#
# indexes = [R, G, B]
# costs = []
#
# for index in indexes:
#     rgb_list_copy = copy.deepcopy(rgb_list)
#     cost = rgb_list_copy[0][index]
#     print(f'데이터 : {cost}, 인덱스 : {index}')
#
#     for data in rgb_list_copy[1:]:
#
#         data[index] = 1001
#
#         min_data = min(data)
#         min_index = data.index(min_data)
#         index = min_index
#         cost += min_data
#
#         print(f'데이터 : {min_data}, 인덱스 : {min_index}')
#
#     costs.append(cost)
#     print()
#
# print((costs))

# RGB 거리
N = int(input())
dp = []

for _ in range(N):
    dp.append(list(map(int, input().split())))

for n in range(1, N):
    dp[n][0] += min(dp[n-1][1], dp[n-1][2])
    dp[n][1] += min(dp[n-1][0], dp[n-1][2])
    dp[n][2] += min(dp[n-1][0], dp[n-1][1])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

