
def dfs(input_graph, start_node):
    visited = []
    need_visit = [start_node]

    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(input_graph[node], reverse=True))

    return visited


def bfs(input_graph, start_node):
    visited = []
    need_visit = [start_node]

    while need_visit:
        node = need_visit.pop(0)

        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(input_graph[node]))

    return visited


N, M, V = list(map(int, input().strip().split(' ')))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().strip().split(' '))
    graph[u].append(v)
    graph[v].append(u)


visited_dfs = dfs(graph, V)
visited_bfs = bfs(graph, V)

for dfs in visited_dfs:
    print(dfs, end=' ')

print()

for bfs in visited_bfs:
    print(bfs, end=' ')

'''
    답은 맞기 했는데 정렬하는 부분에서 
    for g in graph:
        g.sort()
    이렇게 한뒤에 dfs, bfs 를 수행하면 더 쉽다.
'''

