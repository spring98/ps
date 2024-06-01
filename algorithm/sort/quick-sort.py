# 기준점 (pivot) 을 정해서, 기준점보다 작은 데이터는 왼쪽, 큰 데이터는 오른쪽으로 모으는 함수를 작성
# 각 왼쪽 오른쪽은 재귀용법을 사용해서 다시 동일 함수를 호출하여 위 작업을 반복함
# divide and conquer
# 평균 > nlogn, 최악 > n^2

import random

def quickSort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = []
    right = []
    for i in range(1, len(data)):
        ref = data[i]
        if ref < pivot:
            left.append(ref)
        else:
            right.append(ref)

    return quickSort(left) + [pivot] + quickSort(right)

unOrdered = random.sample(range(100), 10)
print(unOrdered)

ordered = quickSort(unOrdered)
print(ordered)
