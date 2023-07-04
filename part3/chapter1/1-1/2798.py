import itertools

# 파이썬은 1초에 20,000,000회 연산,, c++ 에 비하면 느리긴 함.

N, M = list(map(int, input().split(' ')))
card_list = list(map(int, input().split(' ')))

permutations_card = list(itertools.permutations(card_list, 3))

max_card = -1
for a, b, c in permutations_card:
    card_sum = a+b+c
    if M >= card_sum > max_card:
        max_card = card_sum

print(max_card)

'''
python 3중 for 문
for i in range(0, length):
    for j in range(i+1, length):
        for k in range(j+1, length):

result = max(result, sum_value)
'''