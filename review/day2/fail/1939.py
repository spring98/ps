# 골드 2

#
# N, M = 3, 3
# input_data = [
#     (1, 2, 2),
#     (3, 1, 3),
#     (2, 3, 2),
# ]
#
# query_start, query_end = 2, 1
#
# graph = [[] for _ in range(N+1)]
#
# for data in input_data:
#     u, v, iw = data
#     graph[u].append((v, iw))
#     graph[v].append((u, iw))
#
# print(graph)
#
#
# def bfs(input_graph, start_node, end_node):
#     visited = [0 for _ in range(N+1)]
#     need_visit = [(start_node, 0)]
#
#     while need_visit:
#         node, weight = need_visit.pop(0)
#
#         if node == end_node:
#             print(weight)
#             break
#
#         if visited[node] == 0:
#             for n, w in input_graph[node]:
#                 need_visit.append((n, max(w, w+weight)))
#             visited[node] = 1
#
#
# bfs(graph, query_start, query_end)
#
import heapq
#
# N = 5
# M = 14
#
graph = [
    [],
    [(2, 5)],
    [(1, 5), (4, 1), (4, 2), (3, 3)],
    [(2, 3)],
    [(2, 1), (2, 2)],
]


def dijkstra2(input_graph, start):
    distances = [float('inf') for _ in range(6)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        print(queue)
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in input_graph[current_node]:
            distance = current_distance + weight
            print(f'adj, weight : {adjacent, weight}, distance, distances[adj] : {distance, distances[adjacent]}')

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances


print(dijkstra2(graph, 1))

