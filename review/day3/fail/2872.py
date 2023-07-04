# 실버 2

import sys
input = sys.stdin.readline

N = int(input())
dp = []
input_data = []
for _ in range(N):
    input_data.append(int(input()))

answer = 0
is_sorted = False
while True:
    for i in range(N-1):
        is_sorted = True
        if input_data[i] > input_data[i+1]:
            is_sorted = False
            input_data.insert(0, input_data.pop(i+1))
            answer += 1
            break
    if is_sorted:
        break

print(answer)


