# 골드 4

y_count, x_count = map(int, input().split())
alphabet_map = [['-'] * y_count for _ in range(x_count)]

# print(alphabet_map)
input_data = [
    # ['C', 'A', 'A', 'B'],
    # ['A', 'D', 'C', 'B'],
]

for j in range(y_count):
    input_data.append(list(input()))

for i in range(x_count):
    for j in range(y_count):
        alphabet_map[i][j] = input_data[j][i]
    #     print(input_data[j][i], end='')
    # print()


# for j in range(y_count):
#     for i in range(x_count):
#         print(alphabet_map[i][j], end='')
#     print()


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


answers = []
def bfs(current_x, current_y):
    visited = [(current_x, current_y)]
    need_visit = [(current_x, current_y, alphabet_map[current_x][current_y], 1)]

    while need_visit:
        x, y, path, weight = need_visit.pop(0)
        print(path)
        for index in range(4):
            nx = x + dx[index]
            ny = y + dy[index]

            if (0 <= nx < x_count) and (0 <= ny < y_count):
                # print((nx, ny), path, alphabet_map[nx][ny])

                # if alphabet_map[nx][ny] in path:
                #     # print(weight, path, alphabet_map[nx][ny], visited, (nx, ny))
                #     print(path)
                #     answers.append(weight)
                #     break
                if alphabet_map[nx][ny] not in path:
                    need_visit.append((nx, ny, path+alphabet_map[nx][ny], weight+1))
                    visited.append((nx, ny))

    return visited


bfs(0, 0)
print(answers)

# q = set()
# q.add((0, 1, 'sesdfsdfsdf'))
# q.add((0, 1, 'ssdfsdfsdf'))
#
# print(q)

