import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = list(map(int, input().strip().split(' ')))
    graph[u].append(v)
    graph[v].append(u)


def bfs(input_graph, start_node):
    visited = []
    need_visit = [(start_node, 0)]

    while need_visit:
        node, w = need_visit.pop(0)

        if node not in visited:
            # print(f'node, w : {node, w}')
            if w > 2:
                # print(len(visited)-1)
                return len(visited)-1

            for n in input_graph[node]:
                need_visit.append((n, w+1))
            visited.append(node)

    return 0


print(bfs(graph, 1))


