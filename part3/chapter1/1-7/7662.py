import sys
import heapq
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    min_heap = []
    for _ in range(n):
        input_data = input().strip().split(' ')
        command, value = input_data[0], int(input_data[1])

        if command == 'I':
            heapq.heappush(min_heap, value)
        elif command == 'D':
            if min_heap:
                if value == 1:
                    for index, value in enumerate(min_heap):
                        if value == max(min_heap):
                            min_heap.pop(index)

                elif value == -1:
                    heapq.heappop(min_heap)

    if not min_heap:
        print('EMPTY')
    else:
        min_value = heapq.heappop(min_heap)
        max_value = -1
        for index, value in enumerate(min_heap):
            if value == max(min_heap):
                max_value = min_heap.pop(index)

        print(f'{max_value} {min_value}')

'''
    time limit 걸림
    해설 : min_heap 과 max_heap 을 따로 구현하여 사용하면 되는데
    mip_heap 과 max_heap 의 데이터의 싱크를 맞춰야 한다.
'''