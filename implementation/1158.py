from collections import deque

N, K = map(int, input().split())
yosepooth_list = [i for i in range(1, N+1)]
yosepooth_deque = deque(yosepooth_list)

answer = []

while yosepooth_deque:
    yosepooth_deque.rotate(-(K-1))
    answer.append(str(yosepooth_deque.popleft()))

tmp = ', '.join(answer)
print(f'<{tmp}>')
