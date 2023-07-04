import sys
import heapq
input = sys.stdin.readline

N = 8
input_data = [
    [6, 15, 21],
    [7, 20, 25],
    [1, 3, 8],
    [3, 2, 14],
    [8, 6, 27],
    [2, 7, 13],
    [4, 12, 18],
    [5, 6, 20]
]

min_heap = []
for data in input_data:
    _, min_value, max_value = data
    heapq.heappush(min_heap, (min_value, max_value))

while min_heap:
    print(heapq.heappop(min_heap))

'''
    해설
    1. (시작시간, 종료시간) 형태로 삽입 정렬(우선순위 큐) - 기존 우선순위 큐
    2. 우선순위 큐를 하나 더 준비 - 새 우선순위 큐
    3. 첫번째 강의를 꺼내 새 우선순위 큐에 종료시간을 담는다.
    아래를 반복한다.
        1. 새 우선순위 큐에서 강의를 꺼낸다.
        2. 기존 우선순위 큐에서 강의를 꺼내 시작 시간과 새 우선순위 큐의 강의의 값과 비교하여 강의 시작시간이 
            더 먼저라면 시간이 겹치므로 새로운 강의실을 배정한다.
                heap.push 2번
            아니라면 기존강의실에 덮어버린다.
                heap.push 1번 
'''