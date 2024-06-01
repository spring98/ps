# 리스트를 절반으로 잘라 비슷한 크기의 두 부분 리스트로 나눈다.
# 각 부분 리스틀르 재귀적으로 합병 정렬을 이용해 정렬한다.
# 두 부분 리스트를 다시 하나의 정렬된 리스트로 합병한다.
#

import random

def split(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    return mergeSort(split(data[:mid]), split(data[mid:]))

def mergeSort(left, right):
    merged = []

    lp = 0
    rp = 0
    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            merged.append(left[lp])
            lp += 1
        else:
            merged.append(right[rp])
            rp += 1

    while lp < len(left):
        merged.append(left[lp])
        lp += 1

    while rp < len(right):
        merged.append(right[rp])
        rp += 1

    return merged

unOrdered = random.sample(range(100), 10)
# unOrdered = [4, 1, 2, 5]
print(unOrdered)

ordered = split(unOrdered)
print(ordered)
