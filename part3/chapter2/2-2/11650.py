import heapq
import sys
input = sys.stdin.readline

input_data = []
n = int(input().strip())
for _ in range(n):
    data = list(map(int, input().strip().split(' ')))
    input_data.append(data)

answer = []
for data in input_data:
    heapq.heappush(answer, (data[0], data[1]))

while answer:
    x, y = heapq.heappop(answer)
    print(f'{x} {y}')




