'''
    4 3

    1 2 3 4
    2 3 4 5
    3 4 5 6
    4 5 6 7

    2 2 3 4 -> 27
    3 4 3 4 -> 6
    1 1 4 4 -> 64
'''

# N, M = 4, 3
N, M = list(map(int, input().split()))
input_data = [
    # [1, 2, 3, 4],
    # [2, 3, 4, 5],
    # [3, 4, 5, 6],
    # [4, 5, 6, 7],
]

query = [
    # [2, 2, 3, 4]
]

for _ in range(N):
    input_data.append(list(map(int, input().split())))

for _ in range(M):
    query.append(list(map(int, input().split())))

dp = [0 for _ in range(N * N + 1)]

for i in range(N):
    for j in range(N):
        dp[(i-1+1) * N + j+1] = dp[(i-1+1) * N + j+1 - 1] + input_data[i][j]

print(dp)

for x1, y1, x2, y2 in query:
    if x2 == x1 and y2 == y1:
        print(dp[(x2 - 1) * N + y2] - dp[(x1 - 1) * N + y1 - 1])
    else:
        print(dp[(x2 - 1) * N + y2] - dp[(x1 - 1) * N + y1])

    # post = dp[(x2 - 1) * N + y2]
    # pre = dp[(x1 - 1) * N + y1]
    # print(post)
    # print(pre)
    # print(post - pre)





