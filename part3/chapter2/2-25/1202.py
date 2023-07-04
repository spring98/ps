N, K = 3, 2
jewels = [(65/1, 1, 65), (23/5, 5, 23), (99/2, 2, 99)]

# import sys
# input = sys.stdin.readline
#
# N, K = list(map(int, input().split()))
# jewels = []
# for _ in range(N):
#     m, v = list(map(int, input().split()))
#     jewels.append((v/m, m, v))

jewels.sort(reverse=True)

bags = [10, 2]
# bags = []
# for _ in range(K):
#     m = int(input())
#     bags.append(m)
bags.sort()

# print(jewels)
# print(bags)

# total_price = 0
# for bag in bags:
#     for i, jewel in enumerate(jewels):
#         w, kg, price = jewel
#         if kg <= bag:
#             total_price += price
#             jewels.pop(i)


total_price = 0
for bag in bags:
    for i, jewel in enumerate(jewels):
        w, kg, price = jewel
        if kg <= bag:
            total_price += price
            jewels.pop(i)
            break
    if not jewels:
        break

print(total_price)

'''
    이중 for 문을 이용하면 O(n2) 으로 시간초과가 발생하기 때문에 우선순위 큐 구조를 이용한다.
    1. 각 보석(무게)과 가방(허용량)을 오름차순으로 정렬한다.
    2. 가방을 하나씩 차례대로 확인한다.
        해당 가방에 들어갈 수 있는 모든 보석들을 가격만 우선순위 큐에 넣는다.
        전부다 넣고 맨위에 가격이 제일 큰 녀석만 뽑는다.
        여러개 넣고 하나뽑고를 반복하면 하나의 가방에 하나의 보석만 담기고
        가장 비싸게 담을 수 있다.
'''