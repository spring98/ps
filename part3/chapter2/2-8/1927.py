import sys
input = sys.stdin.readline
import heapq

n = int(input().strip())
min_heap = []

for _ in range(n):
    data = int(input().strip())
    if data == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, data)

