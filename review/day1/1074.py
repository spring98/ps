# 실버 1

N = 2

z_table = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        print(z_table[i][j], end=' ')
    print()


def recursion(x, y):
    recursion(x/2, y)
    recursion(x, y/2)
    recursion(x/2, y/2)



