def dfs(input_graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.append(node)
            need_visit.extend(input_graph[node])
    return visited



N = 6
M = 5
graph = [[] for _ in range(N+1)]
input_data = [(1, 2), (2, 5), (5, 1), (3, 4), (4, 6)]

for data in input_data:
    u, v = data
    graph[u].append(v)
    graph[v].append(u)

print(graph)
print(dfs(graph, 1))
