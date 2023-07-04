import heapq
import sys
input = sys.stdin.readline

n = int(input().strip())
min_heap = []

for _ in range(n):
    heapq.heappush(min_heap, int(input().strip()))

total_sum = 0
sub_sum = 0
first_flag = True
first_value = 0

while min_heap:
    if first_flag:
        data = heapq.heappop(min_heap)
        first_flag = False
        first_value = data
    else:
        data = heapq.heappop(min_heap)

    sub_sum += data
    total_sum += sub_sum

if n == 1:
    print(first_value)
else:
    print(total_sum-first_value)

'''
    접근은 맞았는데 구현에서 막혔다.
    해설
    접근했던 것 처럼 제일 작은 수부터 계속 더해가면 된다.
    이때 두개를 꺼내서 더한다음에 다시 최소힙에 넣어서 계산해야 한다.
    원래 접근했던 것 처럼하게되면 앞에 2개 더한 수가 엄청크고 다음 수가 작다면 틀린 답이 될 수 도 있기 때문이다.
'''
