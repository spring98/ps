x_count, y_count, K = 10, 8, 17

# map 을 생성할 때는 x와 y를 반대로 생성해야 [x][y]로 접근할 수 있다.
cabbage_map = [[0] * y_count for _ in range(x_count)]
input_data = [
    [0, 0],
    [1, 0],
    [1, 1],
    [4, 2],
    [4, 3],
    [4, 5],
    [2, 4],
    [3, 4],
    [7, 4],
    [8, 4],
    [9, 4],
    [7, 5],
    [8, 5],
    [9, 5],
    [7, 6],
    [8, 6],
    [9, 6],
]


for ix, iy in input_data:
    cabbage_map[ix][iy] = 1

for i in range(y_count):
    for j in range(x_count):
        print(cabbage_map[j][i], end=' ')
    print()


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = []
answer = 0


def bfs(current_x, current_y):
    global answer
    need_visit = [(current_x, current_y)]
    local_visited = []

    while need_visit:
        x, y = need_visit.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < x_count) and (0 <= ny < y_count) and ((nx, ny) not in visited and (cabbage_map[nx][ny] == 1)):
                need_visit.append((nx, ny))
                visited.append((nx, ny))
                local_visited.append((nx, ny))

    if local_visited:
        answer += 1


for i in range(x_count):
    for j in range(y_count):
        bfs(i, j)

print(answer)

'''
    
y_count, x_count, K = 3, 4, 5
trash_map = [[0] * y_count for _ in range(x_count)]
input_data = [
    [3, 2],
    [2, 2],
    [3, 1],
    [2, 3],
    [1, 1],
]

print(trash_map)

# 이건 문제가 좀 이상 해서 그럼
for iy, ix in input_data:
    trash_map[ix-1][iy-1] = 1
print(trash_map)


for i in range(y_count):
    for j in range(x_count):
        print(trash_map[j][i], end=' ')
    print()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 0
visited = []


def DFS(current_x, current_y):
    global answer

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


for i in range(x_count):
    for j in range(y_count):
        # print(f'(i, j) : {i, j}', end=' ')
        print(i, j, ': ', DFS(i, j))
    # print()

# print(answer)

'''