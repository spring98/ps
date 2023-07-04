import sys
from collections import deque

input = sys.stdin.readline

N, K = list(map(int, input().strip().split(' ')))

deq = deque()
answer = []

for i in range(1, N+1):
    deq.append(i)

for _ in range(N):
    deq.rotate(-K+1)
    answer.append(deq.popleft())

answer_str = ', '.join(str(e) for e in answer)
print(f'<{answer_str}>')
