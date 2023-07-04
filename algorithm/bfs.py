def bfs(input_graph, start_node):
    visited = []
    need_visit = [start_node]

    while need_visit:
        node = need_visit.pop(0)

        if node not in visited:
            visited.append(node)
            need_visit.extend(input_graph[node])
            # need_visit.extend(sorted(input_graph[node]))

    return visited
