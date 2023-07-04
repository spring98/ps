import sys
import heapq
input = sys.stdin.readline

input_data = input().strip()

max_heap = []

for data in input_data:
    int_data = int(data)
    heapq.heappush(max_heap, -int_data)

while max_heap:
    print(-heapq.heappop(max_heap), end='')

