

dp = [[0]*1001 for _ in range(1001)]
n = int(input())

# input_data = [10, 20, 10, 30, 20, 50]
input_data = list(map(int, input().split(' ')))

count = 1
prev_data = -1
for i in range(n):
    for j in range(i, n):
        # print(input_data[j], end=' ')
        if prev_data < input_data[j]:
            dp[i][j] = count
            prev_data = input_data[j]
            count += 1
    # print()
    count = 1
    prev_data = -1

# print(dp)
answer = []
for i in range(n):
    answer.append(dp[i][n-1])

print(max(answer))

'''
    해설
    LIS(Longest Increasing Subsequence) 문제
    D[i] = array[i] 를 마지막 원소로 가지는 부분 수열의 최대길이
    모든 0 <= ㅓ <i 에 때하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
    1차원 dp 테이블 .. 
'''

