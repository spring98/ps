# 실버 2

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    input_data = list(map(int, input().split()))

    money = 0
    count = 0
    for i in range(N):
        if i == N-1:
            money += (input_data[i] * count)
            count = 0
        else:
            if input_data[i] <= input_data[i+1]:
                money -= input_data[i]
                count += 1
            else:
                money += (input_data[i] * count)
                count = 0

    print(money)
