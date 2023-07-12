
N = int(input())

dp = [0] * 100

dp[0], dp[1] = 1, 1
for i in range(N):
    dp[i+2] = dp[i+1] + dp[i]

print(dp[N-1])
