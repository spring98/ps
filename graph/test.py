
y_count, x_count, K = 3, 4, 5

input_data = [
    [3, 2],
    [2, 2],
    [3, 1],
    [2, 3],
    [1, 1],
]

trash_map = [
    [0] * y_count for _ in range(x_count)
]

print(trash_map)

for iy, ix in input_data:
    trash_map[ix-1][iy-1] = 1


for i in range(y_count):
    for j in range(x_count):
        print(trash_map[j][i], end=' ')
    print()


visited = []


def dfs(current_x, current_y):
    need_visit = [(current_x, current_y)]
    local_visit = []

    while need_visit:
        x, y = need_visit.pop()
        if 0 <= x < x_count and 0 <= y < y_count and (x, y) not in visited and trash_map[x][y] == 1:
            need_visit.extend([(x+1, y), (x, y+1), (x-1, y), (x, y-1)])
            visited.append((x, y))
            local_visit.append((x, y))

    return local_visit


for i in range(x_count):
    for j in range(y_count):
        print(dfs(i, j))





