

from itertools import combinations_with_replacement as H
# def divide(n, m):
#     for x in H(range(n+1), m):
#         if sum(x) == n:
#             print(x, end=' ')
# divide(4, 2)

from itertools import product, combinations


def prod(n, m):
    return_list = []
    for i in product(range(n+1), repeat=m):
        if sum(i) == n:
            return_list.append(i)

    return return_list


L = 4
C = 6

naturals = prod(L, 2)
print(naturals)

# [mo, ja]
# a t c i s w
mos = ['a', 'e']
jas = ['c', 's', 't', 'w']

combis = []
for natural in naturals:
    mo_count, ja_count = natural
    if mo_count >= 1 and ja_count >= 2:
        combis.append((mo_count, ja_count))

print(combis)

for combi in combis:
    mo, ja = combi

    for i in combinations(mos, mo):
        print(i)

    for i in combinations(jas, ja):
        print(i)






