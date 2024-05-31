# import heapq
#
# graph2 = {
#     'A': {'B': 8, 'C': 1, 'D': 2},
#     'B': {},
#     'C': {'B': 5, 'D': 2},
#     'D': {'E': 3, 'F': 5},
#     'E': {'F': 1},
#     'F': {'A': 5},
# }
#
#
# def dijkstra(input_graph, start):
#     distances = {node: float('inf') for node in input_graph}
#     distances[start] = 0
#     queue = []
#     heapq.heappush(queue, [distances[start], start])
#
#     while queue:
#         current_distance, current_node = heapq.heappop(queue)
#
#         if distances[current_node] < current_distance:
#             continue
#
#         for adjacent, weight in input_graph[current_node].items():
#             distance = current_distance + weight
#
#             if distance < distances[adjacent]:
#                 distances[adjacent] = distance
#                 heapq.heappush(queue, [distance, adjacent])
#
#     return distances
#
#
# print(dijkstra(graph2, 'A'))
# print(dijkstra(graph2, 'B'))
# print(dijkstra(graph2, 'C'))
# print(dijkstra(graph2, 'D'))
# print(dijkstra(graph2, 'E'))
# print(dijkstra(graph2, 'F'))

# dict stdin 으로 넣을 때 default 로 만들어주면 된다.
# for _ in range(M):
#     u, v, w = list(map(int, input().strip().split()))
#     # graph[u][v] = w
#     graph[u] = {v: w}
#     print(graph)


# 리스트 버전

import heapq
#
# N = 5
# M = 14
#
graph = [
    [],
    [(2, 2), (3, 3), (4, 1), (5, 10), (4, 2)],
    [(4, 2)],
    [(4, 1), (5, 1), (5, 10), (1, 8), (4, 2)],
    [(5, 3)],
    [(1, 7), (2, 4)],
]


def dijkstra2(input_graph, start):
    # 6 하드코딩
    distances = [float('inf') for _ in range(6)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in input_graph[current_node]:
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances


print(dijkstra2(graph, 1))
print(dijkstra2(graph, 2))
print(dijkstra2(graph, 3))
print(dijkstra2(graph, 4))
print(dijkstra2(graph, 5))

