# 앞의 두개씩 비교한다
# 뒤의 값이 더 크다면 패스
# 뒤의 값이 더 작다면 스왑

import random

def bubbleSort(unOrderedList):
    for i in range(len(unOrderedList) - 1):
        swap = False
        for j in range(len(unOrderedList) - i - 1):
            if unOrderedList[j+1] < unOrderedList[j]:
                unOrderedList[j], unOrderedList[j+1] = unOrderedList[j+1], unOrderedList[j]
                swap = True

        if not swap:
            break

    return unOrderedList

unOrderedList = random.sample(range(100), 10)
print(unOrderedList)

orderedList = bubbleSort(unOrderedList)
print(orderedList)
