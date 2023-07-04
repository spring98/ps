# 카드 구매 하기

N = 4

weight_limit = 4
price_list = [1, 5, 6, 7]
weight_list = [1, 2, 3, 4]

dp = [
    # [0] * (배낭의 최대 무게+1) for _ in range(보석의 갯수+1)
    [0] * (N+1) for _ in range(N+1)
]

print(dp)

# 보석의 갯수
for i in range(N+1):
    # 보석의 무게
    for w in range(N+1):
        # if 무게 초과
        if weight_list[i-1] <= w:
            dp[i][w] = max(dp[i - 1][w], price_list[i-1] + dp[i - 1][w - weight_list[i-1]])
        else:
            dp[i][w] = dp[i - 1][w]

print(dp)
print(dp[N][weight_limit])

