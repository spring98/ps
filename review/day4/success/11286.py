# 실버 1

import heapq
import sys
input = sys.stdin.readline

N = int(input())

abs_min_heap = []

for _ in range(N):
    data = int(input())
    if data == 0:
        if abs_min_heap:
            absolute_data, real_data = heapq.heappop(abs_min_heap)
            print(real_data)
        else:
            print(0)
    else:
        heapq.heappush(abs_min_heap, (abs(data), data))

