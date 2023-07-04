import heapq
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
start_node = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = list(map(int, input().strip().split()))
    graph[u].append((v, w))


# graph = [
#     [],
#     [(2, 2), (3, 3), (4, 1), (5, 10), (4, 2)],
#     [(4, 2)],
#     [(4, 1), (5, 1), (5, 10), (1, 8), (4, 2)],
#     [(5, 3)],
#     [(1, 7), (2, 4)],
# ]

def dijkstra2(input_graph, start):
    distances = [float('inf') for _ in range(N+1)]
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


answers = dijkstra2(graph, start_node)[1:N+1]
for answer in answers:
    if answer == float('inf'):
        print('INF')
    else:
        print(answer)








