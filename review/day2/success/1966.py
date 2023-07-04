from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    N, M = map(int, input().split())

    input_data = list(map(int, input().split()))
    printer = deque([])

    for i, priority in enumerate(input_data):
        printer.append((priority, i))

    count = 1
    while printer:
        if printer[0][0] < max(printer)[0]:
            printer.rotate(-1)
        else:
            index = printer.popleft()[1]
            if index == M:
                print(count)
                break
            count += 1
