# 4 2
# 2 1 2
# 4 3 2
# 1 4 3
# 1 2
# 3 2

N = 4
graph = [
    [],
    [(2, 2), (4, 3)],
    [(1, 2)],
    [(4, 2)],
    [(3, 2), (1, 3)],
]

print(graph)
count = 0
distance = [-1] * (N+1)


def dfs(input_graph, start_node, end_node):
    visited = []
    need_visit = [(start_node, 0)]
    weights = 0
    min_weight = 1000000

    while need_visit:
        tup = need_visit.pop()
        node, weight = tup

        if node not in visited:
            need_visit.extend(input_graph[node])
            visited.append(node)
            distance[node] = distance[start_node] + weight

            # if node == end_node:
            #     break

    return visited


# print(dfs(graph, 1, 2))
# print(distance)

print(dfs(graph, 3, 2))
print(distance)


'''
    원래 그래프에서 최단거리를 구하려면 BFS 를 이용해야 하지만
    이녀석은 트리 이기때문에 cyclic 이 일어나지 않음으로 그냥 DFS 로 구해도 된다. 
    최단거리를 구할때는 
    while queue:
        v, d = queue.popleft()
        
        if v == find: #찾는 노드와 번호가 일치하면 거리 리턴
            return d
        
        for i, l in graph[v]: #연관된 노드에 대한 노드번호와 간선길이
            if not visited[i]:
                visited[i] = True
                queue.append((i,d+l)) #지금까지 노드를 찾으면서 거리를 기록
    이런식으로 지금까지 거리 + 현재 weight 거리 해서 리턴하면 된다.
    
'''




