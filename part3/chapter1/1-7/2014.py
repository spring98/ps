from itertools import combinations_with_replacement
import heapq
import sys
input = sys.stdin.readline

K, N = map(int, input().strip().split(' '))
input_data = list(map(int, input().strip().split(' ')))
min_heap = []
for_count = 1
while for_count != K+1:
    for cwr in combinations_with_replacement(input_data, for_count):
        product = 1
        for item in cwr:
            product *= item
        heapq.heappush(min_heap, product)
    for_count += 1

# print(min_heap)
print(heapq.nsmallest(N, min_heap)[-1])



# input_data = [2, 3, 5, 7]
# min_heap = []
# for_count = 1
# # while len(min_heap) < 38:
# while for_count != 5:
#     for cwr in combinations_with_replacement(input_data, for_count):
#         product = 1
#         for item in cwr:
#             product *= item
#         heapq.heappush(min_heap, product)
#     for_count += 1
#
# print(min_heap)
# print(heapq.nsmallest(19, min_heap))

'''
    메모리초과
    해설 
    1. 최소힙에 처음 부여받은 소수를 입력
    2. top 원소(최소값)를 꺼낸다.
    3. 부여받은 소수들과 곱해서 다시 넣는다.
    단, 힙의 크기가 N이상이고, 힙의 최대값보다 곱한 결과가 크다면 무시한다.
        한번 구한 결과는 힙에 넣지 않아도 된다. 
    
'''