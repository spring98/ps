# 지름길

import heapq

graph = [
    [] for _ in range(200)
]


graph[0].append((50, 10))
graph[0].append((150, 150))

graph[50].append((100, 10))
graph[50].append((150, 100))

graph[100].append((151, 10))
graph[100].append((150, 50))

graph[110].append((140, 10))
graph[110].append((150, 40))

graph[140].append((150, 10))


def dijkstra(input_graph, start):
    distances = [float('inf') for _ in range(200)]
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


print(dijkstra(graph, 0)[150])



# graph = [
#     [],
#     [(2, 2), (3, 3), (4, 1), (5, 10), (4, 2)],
#     [(4, 2)],
#     [(4, 1), (5, 1), (5, 10), (1, 8), (4, 2)],
#     [(5, 3)],
#     [(1, 7), (2, 4)],
# ]
#
# print(dijkstra(graph, 1))
# print(dijkstra(graph, 2))
# print(dijkstra(graph, 3))
# print(dijkstra(graph, 4))
# print(dijkstra(graph, 5))
#
# answer
#     [inf, 0, 2, 3, 1, 4]
#     [inf, 12, 0, 15, 2, 5]
#     [inf, 8, 5, 0, 1, 1]
#     [inf, 10, 7, 13, 0, 3]
#     [inf, 7, 4, 10, 6, 0]


