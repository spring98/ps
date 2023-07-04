# 실버 1

import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    input_data = list(map(int, input().split()))

    input_data.sort()

    arr1, arr2 = [], []

    arr1.append(input_data.pop(0))
    arr2.append(input_data.pop(0))

    max_heap = []

    while input_data:
        pop_data = input_data.pop(0)
        if arr1[-1] < arr2[-1]:
            heapq.heappush(max_heap, -abs(pop_data - arr1[-1]))
            arr1.append(pop_data)

        else:
            heapq.heappush(max_heap, -abs(pop_data - arr2[-1]))
            arr2.append(pop_data)

    heapq.heappush(max_heap, -abs(arr1[0] - arr2[0]))
    heapq.heappush(max_heap, -abs(arr1[-1] - arr2[-1]))

    print(-heapq.heappop(max_heap))
