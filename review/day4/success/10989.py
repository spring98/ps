import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 10001

for _ in range(N):
    dp[int(input())] += 1

for i, d in enumerate(dp):
    if d == 0:
        continue
    for _ in range(d):
        print(i)
