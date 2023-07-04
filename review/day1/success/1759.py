# 4 6
# a t c i s w
from itertools import combinations

L, C = map(int, input().split())
input_data = list(input().split())
input_data.sort()

mos = ['a', 'e', 'i', 'o', 'u']

for datas in combinations(input_data, L):
    mo_count = 0
    for mo in mos:
        if mo in datas:
            mo_count += 1

    if mo_count >= 1 and L-mo_count >= 2:
        for data in datas:
            print(data, end='')
        print()
