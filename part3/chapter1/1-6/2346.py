import sys
from collections import deque

input = sys.stdin.readline
deq = deque()

N = int(input())

# targets = [3, 2, 1, -3, -1]
targets = list(map(int, input().strip().split(' ')))
answer = []
for i, target in enumerate(targets):
    deq.append((i+1, target))

while deq:
    index, target = deq.popleft()

    if target > 0:
        deq.rotate(target-1)
    else:
        deq.rotate(target)
    answer.append(index)

for ans in answer:
    print(ans, end=' ')

'''
    틀렸다고 나오는데 이유를 모르겠다.
'''