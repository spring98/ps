
y_count, x_count, K = list(map(int, input().split()))

# print(y_count, x_count, K)

trash_map = [[0] * y_count for _ in range(x_count)]
# input_data = [
#     [3, 2],
#     [2, 2],
#     [3, 1],
#     [2, 3],
#     [1, 1],
# ]
input_data = []

for _ in range(K):
    input_data.append(list(map(int, input().split())))

# print(trash_map)

# 이건 문제가 좀 이상 해서 그럼
for iy, ix in input_data:
    trash_map[ix-1][iy-1] = 1
# print(trash_map)


# for i in range(y_count):
#     for j in range(x_count):
#         print(trash_map[j][i], end=' ')
#     print()

visited = []


def DFS(current_x, current_y):
    need_visit = [(current_x, current_y)]
    local_visited = []

    while need_visit:
        x, y = need_visit.pop()
        if (x, y) not in visited:
            if (0 <= x < x_count) and (0 <= y < y_count) and (trash_map[x][y] == 1):
                need_visit.extend([(x+1, y), (x, y+1), (x-1, y), (x, y-1)])
                visited.append((x, y))
                local_visited.append((x, y))

    return local_visited


answer_list = []
for i in range(x_count):
    for j in range(y_count):
        answer_list.append(len(DFS(i, j)))

print(max(answer_list))

