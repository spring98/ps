
N, M = 2, 3
input_data = [
    [1, 2, 4],
    [8, 16, 32],
]

K = 3

querys = [
    [1, 1, 2, 3],
    [1, 2, 1, 2],
    [1, 3, 2, 3],
]

print(input_data[0][0], input_data[1][2])

i, j, x, y = (1, 1, 2, 3)
for index in range(i-1, x):
    print(input_data[index])

# for query in querys:
#     i, j, x, y = query
#     for index in range(i-1, x):
#         print(input_data[index])
#     # input_data

