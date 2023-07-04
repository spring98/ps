# 실버 2

N = int(input())
input_data = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if input_data[i] > input_data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
