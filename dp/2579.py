# 계단 오르기

n = 6

w = [10, 20, 15, 25, 10, 20]
dp = [0 for _ in range(n)]


dp[0] = w[0]
dp[1] = w[0] + w[1]

for i in range(3, n):
    dp[i] = max(w[i] + w[i-1] + dp[i-3], w[i] + dp[i-2])
    # print(i)
    print(dp)

print("=====")
print(dp)



