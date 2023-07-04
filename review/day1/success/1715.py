import heapq
import sys
input = sys.stdin.readline

N = int(input())

cards = []

for _ in range(N):
    heapq.heappush(cards, int(input()))

count = 0
while len(cards) >= 2:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    count += (a + b)
    heapq.heappush(cards, a+b)

print(count)








