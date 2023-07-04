import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * N for _ in range(N)]
for i in range(N):
    for j, data in enumerate(list(map(int, input().split()))):
        # print(j, i)
        if (i-1) < 0:
            dp[i][j] = data
            break

        if (j-1) < 0:
            dp[i][j] = dp[i-1][j] + data
        else:
            dp[i][j] = max(dp[i-1][j-1] + data, dp[i-1][j] + data)

print(max(dp[-1]))









