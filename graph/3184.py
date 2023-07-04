import sys
input = sys.stdin.readline

y_count, x_count = list(map(int, input().strip().split()))

input_data = [
    # '.###.#####..',
    # '#.oo#...#v#.',
    # '#..o#.#.#.#.',
    # '#..##o#...#.',
    # '#.#v#o###.#.',
    # '#..#v#....#.',
    # '#...v#v####.',
    # '.####.#vv.o#',
    # '.......####.',
]

for _ in range(y_count):
    input_data.append(input().strip())

# print(input_data)

ground_map = [
    ['-'] * y_count for _ in range(x_count)
]

# print(ground_map)
#
# for i in range(y_count):
#     for j in range(x_count):
#         print(ground_map[j][i], end=' ')
#     print()
#
#
# for i in range(y_count):
#     for j in range(x_count):
#         print(input_data[i][j], end=' ')
#     print()

for i in range(y_count):
    for j in range(x_count):
        ground_map[j][i] = input_data[i][j]

#
# for i in range(y_count):
#     for j in range(x_count):
#         print(ground_map[j][i], end=' ')
#     print()

# for i in range(x_count):
#     for j in range(y_count):
#         # print(dfs(i, j))
#         dfs(i, j)
visited = [
    [False] * (y_count+1) for _ in range(x_count+1)
]
# print(visited)
global_sheep = 0
global_wolf = 0


def dfs(current_x, current_y):
    global global_sheep, global_wolf
    need_visit = [(current_x, current_y)]
    local_visit = []
    sheep = 0
    wolf = 0

    while need_visit:
        x, y = need_visit.pop()
        # if (x, y) not in visited and 0 <= y < y_count and 0 <= x < x_count and ground_map[x][y] != '#':
        if not visited[x][y] and 0 <= y < y_count and 0 <= x < x_count and ground_map[x][y] != '#':
            need_visit.extend([(x+1, y), (x, y+1), (x-1, y), (x, y-1)])
            local_visit.append((x, y))
            # visited.append((x, y))
            visited[x][y] = True
            if ground_map[x][y] == 'v':
                wolf += 1
            if ground_map[x][y] == 'o':
                sheep += 1

    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0

    global_sheep += sheep
    global_wolf += wolf

    # return f'sheep : {sheep}, wolf : {wolf}'


for i in range(x_count):
    for j in range(y_count):
        # print(dfs(i, j))
        dfs(i, j)
        # print(visited)


print(global_sheep, global_wolf)
