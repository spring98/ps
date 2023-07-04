from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    input_data = deque(list(map(int, input().split())))
    trans_data = deque([0] * N)

    count = 0
    while True:
        for i in range(N):
            if input_data[i] % 2 == 1:
                input_data[i] += 1

            trans_data[i] = input_data[i] // 2
            input_data[i] /= 2
        trans_data.rotate(1)

        for j in range(N):
            input_data[j] += trans_data[j]

        # print(input_data)
        if min(input_data) == max(input_data):
            break

        count += 1

    print(count)