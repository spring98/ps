# 두번째 부터 시작해서 하나씩 인덱스를 증가시킨다.
# 현재 값이 왼쪽 값보다 작으면 클때까지 스왑한다.

import random

def insertionSort(data):
    for i in range(1, len(data)):
        j = i
        while j > 0 and data[j] < data[j - 1]:
            data[j - 1], data[j] = data[j], data[j - 1]
            j -= 1

    return data


# unOrdered = [5, 3, 2, 4]
unOrdered = random.sample(range(100), 20)
print(unOrdered)

ordered = insertionSort(unOrdered)
print(ordered)
