import sys
input = sys.stdin.readline


def dfs(input_graph, start_node):
    visited = []
    need_visit = [start_node]

    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.append(node)
            need_visit.extend(input_graph[node])

    return visited


N = int(input().strip())
M = int(input().strip())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = list(map(int, input().strip().split(' ')))
    graph[u].append(v)
    graph[v].append(u)

print(len(dfs(graph, 1))-1)


