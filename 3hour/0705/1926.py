
# y_count, x_count = 6, 5
# graph = [
#     [1, 1, 0, 1, 1],
#     [0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [1, 0, 1, 1, 1],
#     [0, 0, 1, 1, 1],
#     [0, 0, 1, 1, 1],
# ]

y_count, x_count = list(map(int, input().split()))
graph = []

for _ in range(y_count):
    graph.append(list(map(int, input().split())))

visited = [[0] * 501 for _ in range(501)]
answer = [0]

def dfs(current_x, current_y):
    need_visit = [(current_x, current_y)]
    local_visit = []
    while need_visit:
        x, y = need_visit.pop()
        # print(f'=={x, y, y_count, x_count}==')
        if (0 <= x < y_count) and (0 <= y < x_count) and visited[x][y] == 0 and graph[x][y] == 1:
            need_visit.extend([(x-1, y), (x, y-1), (x+1, y), (x, y+1)])
            visited[x][y] = 1
            local_visit.append((x, y))
    # print(local_visit)
    if local_visit:
        answer.append(len(local_visit))

for i in range(y_count):
    for j in range(x_count):
        # print(graph[i][j], end=' ')
        dfs(i, j)
        # print(i, j, end=' ')
    # print()

print(len(answer)-1)
print(max(answer))
