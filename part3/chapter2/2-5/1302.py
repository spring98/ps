import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())
input_data = []

for _ in range(n):
    input_data.append(input().strip())

input_dict = dict()
for item in input_data:
    if item not in input_dict:
        input_dict[item] = 1
    else:
        input_dict[item] += 1

max_heap = []
for i in input_dict.items():
    heapq.heappush(max_heap, (-i[1], i[0]))

print(heapq.heappop(max_heap)[1])

