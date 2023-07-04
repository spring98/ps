n = 8
graph = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

count_map = [[0] * 9 for _ in range(8)]


def bfs(input_graph, input_x, input_y):

    visited = []
    need_visit = [(0, input_x, input_y)]

    while need_visit:
        w, x, y = need_visit.pop(0)

        if (x, y) not in visited:
            if 0 <= x < n and 0 <= y < n:
                if input_graph[y][x] == 1:
                    dw = 1
                else:
                    dw = 0
                need_visit.extend([(w + dw, x + 1, y), (w + dw, x, y + 1), (w + dw, x - 1, y), (w + dw, x, y - 1)])
                visited.append((w, x, y))
                print(f'x, y, w : {x + 1, y + 1, w}')

    return visited


# print(bfs(graph, 0, 0))
# bfs(graph, 0, 0)

print(count_map)

'''
    큐에서 하나의 원소를 꺼낸 뒤에는 상하좌우 위치를 확인한다.
    인접한 위치에 치즈가 있다면, 치즈가 있는 위치에 대하여 카운트 한다.
    카운트가 2이상인 치즈를 없앤다.
'''