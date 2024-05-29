# 현재 인덱스를 하나씩 증가시키면서 마지막 인덱스까지 거쳐 최소값을 찾는다.
# 시작한 인덱스와 최소값을 가진 인덱스와 스왑한다.

import random

def selectionSort(data):
    for i in range(len(data) - 1):
        minIndex = i
        for j in range(i+1, len(data)):
            if data[j] < data[minIndex]:
                minIndex = j

        data[i], data[minIndex] = data[minIndex], data[i]

    return data

# unOrdered = [5, 4, 2, 3, 1]
unOrdered = random.sample(range(100), 20)
print(unOrdered)

ordered = selectionSort(unOrdered)
print(ordered)
