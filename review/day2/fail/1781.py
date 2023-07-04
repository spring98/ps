# 골드 2

import sys
input = sys.stdin.readline

N = int(input())

input_data = []

for _ in range(N):
    dead, cup = map(int, input().split())
    input_data.append((dead, cup))

input_data.sort(key=lambda x: (x[0], -x[1]))

count = 0
answer = 0
while input_data:
    dead_line, cup = input_data.pop(0)
    if count < dead_line:
        answer += cup
        count += 1

print(answer)
