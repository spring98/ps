# 골드 2

N = 19
input_data = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 6, 7],
    [4, 8, -1],
    [5, 9, 10],
    [6, 11, 12],
    [7, 13, -1],
    [8, -1, -1],
    [9, 14, 15],
    [10, -1, -1],
    [11, 16, -1],
    [12, -1, -1],
    [13, 17, -1],
    [14, -1, -1],
    [15, 18, -1],
    [16, -1, -1],
    [17, -1, 19],
    [18, -1, -1],
    [19, -1, -1],
]

graph = [[] for _ in range(N+1)]
for data in input_data:
    u, v_left, v_right = data
    graph[u].append((v_left, v_right))

print(graph)


def bfs(input_graph, start_node):
    visited = []
    need_visit = [start_node]

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            need_visit.extend(input_graph[node])
            visited.append(node)

    return visited

print(bfs(graph, 1))












