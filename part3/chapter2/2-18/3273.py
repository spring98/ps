from itertools import combinations
import sys
input = sys.stdin.readline

# n = int(input().strip())
# input_data = list(map(int, input().strip().split(' ')))
# x = int(input().strip())
#
# count = 0
# for combination in combinations(input_data, 2):
#     if combination[0] + combination[1] == x:
#         count += 1
#         print(combination)
#
# print(count)

n = int(input().strip())
input_data = list(map(int, input().strip().split(' ')))
x = int(input().strip())
input_data.sort()

count = 0
while input_data:
    ai = input_data.pop(0)
    target = x - ai

    if target < 0:
        break

    if target in input_data:
        input_data.pop(input_data.index(target))
        count += 1


print(count)

'''
    답은 맞긴 맞음 
    해설
    조합으로 푸는 거긴 한데, 그냥 조합으로 풀면 O(n2) 이 되어 시간 초과가 된다.
    그래서 투포인터 알고리즘으로 조합을 구현하여 해결한다.
    시작점과 끝점을 이용해 문제를 해결하는 알고리즘이다.
    초기화 : 시작점(start) = 0, 끝점(end) = N-1
    1. 원소를 오름차순으로 정렬한다.
    2. 정렬이 되어 있기 때문에 
        시작위치를 1만큼 증가시키면 sorted[start] + sorted[end] 가 증가한다.
        끝 위치를 1만큼 감소시키면 sorted[start] + sorted[end] 가 감소한다.
    3. 이러한 방식으로 현재의 합(sorted[start] + sorted[end])과 x를 매번 비교한다. 
        현재의 합이 x보다 작거나 같으면 시작점을 1증가
        현재의 합이 x보다 크면 끝점을 1감소
        같으면 count++
'''

