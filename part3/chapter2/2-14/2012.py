import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
input_data = []
for _ in range(N):
    input_data.append(int(input().strip()))

min_heap = []

for data in input_data:
    heapq.heappush(min_heap, data)

count = 1
score = 0
while min_heap:
    sudo_score = heapq.heappop(min_heap)
    score += abs(count - sudo_score)
    count += 1

print(score)

