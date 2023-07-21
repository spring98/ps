# 가로 N, 세로 M

graph = []

# y_count, x_count = 1, 2
# input_data = [
#     'B',
#     'W'
# ]
# for datas in input_data:
#     data = [i for i in datas]
#     graph.append(data)


y_count, x_count = list(map(int, input().split()))
for _ in range(x_count):
    data = [i for i in input()]
    graph.append(data)


visited = [[False] * (y_count+1) for _ in range(x_count+1)]

# print(visited)
def bfs(input_x, input_y, target):
    local_visit = []
    need_visit = [(input_x, input_y)]

    while need_visit:
        nx, ny = need_visit.pop(0)
        # print(nx, ny)
        if 0 <= nx < x_count and 0 <= ny < y_count and not visited[nx][ny] and graph[nx][ny] == target:
            visited[nx][ny] = True
            local_visit.append((nx, ny))
            need_visit.extend([(nx+1, ny), (nx, ny+1), (nx-1, ny), (nx, ny-1)])

    # print(local_visit)
    return len(local_visit)

answer_w = 0
for i in range(x_count):
    for j in range(y_count):
        return_w = bfs(i, j, 'W')
        answer_w += (return_w*return_w)

answer_b = 0
for i in range(x_count):
    for j in range(y_count):
        return_b = bfs(i, j, 'B')
        answer_b += (return_b * return_b)

print(answer_w, answer_b)







