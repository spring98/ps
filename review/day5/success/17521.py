# 실버 4

import sys
input = sys.stdin.readline

N, W = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

coin = 0
for i in range(N-1):
    if coins[i] < coins[i+1]:
        coin += (W // coins[i])
        W = (W % coins[i])

        W += (coin * coins[i+1])
        coin -= (W // coins[i+1])

    # print(i, coin, W)

print(W)
