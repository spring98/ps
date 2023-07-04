import heapq
import sys
input = sys.stdin.readline

input_data = [1, 5, 4, 3, 2]
min_heap = []

pop_count = 1
for i, data in enumerate(input_data):
    heapq.heappush(min_heap, data)
    print(f'data : {data}')

    index = i+1

    current_count = 0
    if index % 2 == 1:
        while True:
            if pop_count == current_count:
                break
            pop_value = heapq.heappop(min_heap)
            print(pop_value)
            heapq.heappush(min_heap, pop_value)
            current_count += 1
    pop_count += 1
    print()

'''
    해설
    1. 최대힙 - 중앙값 - 최소힙의 구조를 갖춘다.
    2. 새로운 원소가 들어오면 
        1. 중앙값 보다 작거나 같은 원소는 왼쪽의 최대힙에 넣는다.
        2. 중앙값 보다 큰 원소는 오른쪽의 최소힙에 넣는다.
    3. 홀수번째 원소가 입력될때마다 최대 힙과 최소힙의 크기를 동일하게 맞춘다.
        한쪽이 더 크다면 반대편으로 이동시킨다.
'''
