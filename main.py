from itertools import permutations
def solution(matrix_sizes):
    table = []

    for i, matrix in enumerate(matrix_sizes):
        a, b = matrix
        if i == 0:
            table.append(a)

        elif i == len(matrix_sizes)-1:
            table.append(a)
            table.append(b)

        else:
            table.append(a)

    total_sum = 100000000
    for perm in permutations(range(1, len(table)-1), len(table)-2):
        my_table = table.copy()
        my_table_sum = 0
        for p in list(perm):
            prev, cur, next = p-1, p, p+1

            while not my_table[prev]:
                prev -= 1

            while not my_table[next]:
                next += 1

            my_table_sum += my_table[prev] * my_table[cur] * my_table[next]
            my_table[cur] = 0

        total_sum = min(total_sum, my_table_sum)

    return total_sum

# print(f'result: {solution([[5,3],[3,10],[10,6]])}')
print(f'result: {solution([[5,3],[3,10],[10,6],[6,1]])}')
