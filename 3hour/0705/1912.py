# [실패]
import heapq
# n = 10
n = int(input())

# input_data = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]
input_data = list(map(int, input().split()))
prefix_sum = [0] * n

answer = []

# print(input_data)
# print(prefix_sum)

# for i in range(n):
#     prefix_sum[i] = input_data[i]
#     for j in range(i+1, n):
#         prefix_sum[j] = prefix_sum[j-1] + input_data[j]
#     print(prefix_sum)
#     print(max(prefix_sum))
#     heapq.heappush(answer, -max(prefix_sum))
#
# print(-heapq.heappop(answer))

prefix_sum[0] = input_data[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + input_data[i]

# print(prefix_sum)
for i in range(n):
    for j in range(i, n):
        prefix_sum[j] -= input_data[i]
    heapq.heappush(answer, -max(prefix_sum))

print(-heapq.heappop(answer))


