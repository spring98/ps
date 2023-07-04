from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split(' '))

deq = deque()
for i in range(1, N+1):
    deq.append(i)

targets = list(map(int, input().strip().split(' ')))
count = 0

for target in targets:
    index = deq.index(target)

    while True:
        if deq[0] == target:
            break

        else:
            if index <= int(len(deq)/2):
                deq.rotate(-1)
            else:
                deq.rotate(1)
            count += 1
    deq.popleft()

print(count)

'''
    다시풀어보기
'''