# 골드 1

import heapq
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
input_data = list(map(int, input().split()))
min_heap_primes = []
dp = [0] * 1000001

for data in input_data:
    heapq.heappush(min_heap_primes, data)
    dp[data] = 1

answer = 0
for _ in range(N):
    # min_heap_primes = list(set(min_heap_primes))
    # heapq.heapify(min_heap_primes)
    answer = heapq.heappop(min_heap_primes)

    for d in input_data:
        put = answer * d
        if dp[put] == 0:
            heapq.heappush(min_heap_primes, put)
            dp[put] = 1


print(answer)


