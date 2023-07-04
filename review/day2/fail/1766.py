# 골드 2

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

N, M = map(int, input().split())

dp = [i for i in range(N+1)]

for _ in range(M):
    prev, post = map(int, input().split())
    dp[post] = prev

stack = []
count = 0


def recursive(index):
    global count
    count += 1

    if count == N+1:
        return

    if dp[index] == index:
        print(index, end=' ')
        while stack:
            index = stack.pop()
            print(index, end=' ')
        recursive(index + 1)
    else:
        stack.append(index)
        recursive(dp[index])


recursive(1)

