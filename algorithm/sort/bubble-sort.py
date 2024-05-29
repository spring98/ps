# 앞의 두개씩 비교한다
# 뒤의 값이 더 크다면 패스
# 뒤의 값이 더 작다면 스왑

import random

def bubbleSort(data):
    for i in range(len(data) - 1):
        swap = False
        for j in range(len(data) - i - 1):
            if data[j + 1] < data[j]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swap = True

        if not swap:
            break

    return data

unOrdered = random.sample(range(100), 10)
print(unOrdered)

ordered = bubbleSort(unOrdered)
print(ordered)
