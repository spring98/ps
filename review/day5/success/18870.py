# 실버 2

import sys
input = sys.stdin.readline

N = int(input())
input_data = list(map(int, input().split()))

sorted_data = []
for i, data in enumerate(input_data):
    sorted_data.append((data, i))

sorted_data.sort()
# print(sorted_data)

result_data = []
index = 0
for i, data in enumerate(sorted_data):
    u, v = data
    result_data.append((u, v, index))
    if i == N-1:
        continue
    else:
        if sorted_data[i][0] < sorted_data[i+1][0]:
            index += 1

# print(result_data)
result_data.sort(key=lambda x: x[1])
# print(result_data)
for data in result_data:
    print(data[2], end=' ')

