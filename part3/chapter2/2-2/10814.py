import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())

input_data = []
for _ in range(n):
    input_data.append(list(input().strip().split(' ')))

answer = []
for index, data in enumerate(input_data):
    age, name = int(data[0]), data[1]
    heapq.heappush(answer, (age, index, name))

while answer:
    age, index, name = heapq.heappop(answer)
    print(f'{age} {name}')

