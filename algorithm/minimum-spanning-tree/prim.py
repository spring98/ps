from collections import defaultdict
import heapq

edges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (8, 'F', 'E'), (9, 'G', 'E'),
    (11, 'G', 'F'),
]

def prim(start_node, edges):
    mst = []
    adjacent_edges = defaultdict(list)

    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapq.heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heapq.heappop(candidate_edge_list)

        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                # edge[2] -> n2 값
                if edge[2] not in connected_nodes:
                    heapq.heappush(candidate_edge_list, edge)

    return mst

print(prim('A', edges))
