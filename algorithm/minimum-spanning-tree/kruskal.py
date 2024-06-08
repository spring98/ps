graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ],
}

# 특정 노드의 부모 찾기
parent = {}

# 특정 노드의 높이 찾기
rank = {}

def find(node):
    # path compression
    # 본인이 루트노드가 아닐 때
    if parent[node] != node:
        parent[node] = find(parent[node])

    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union by rank
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        # 높이가 같을 때
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = []

    # 초기화
    for node in graph['vertices']:
        make_set(node)

    # 간선 weight sort
    edges = graph['edges']
    edges.sort()

    # 사이클 없는 간선만 연결
    for edge in edges:
        weight, node_v, node_u = edge

        # 루트 노드가 다르다 = 사이클이 생기지 않는다.
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst

print(kruskal(graph))
