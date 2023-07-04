import sys
import heapq
input = sys.stdin.readline

answer = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if len(answer) == 0:
            print(0)
        else:
            abs_value, origin_value = heapq.heappop(answer)
            print(origin_value)
    else:
        heapq.heappush(answer, (abs(x), x))


'''
    아이디어는 맞았는데 구현 실패
'''