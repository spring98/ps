import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(101)]

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
    distances = [float('inf') for _ in range(101)]
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


answers = []
for i in range(1, 101):
    # if dijkstra2(graph, i):
    for data in dijkstra2(graph, i)[1:N+1]:
        if data == float('inf'):
            break
        else:
            answers.append(data)

count = 1
for answer in answers:
    print(answer, end=' ')
    if count % N == 0:
        print()

    count += 1


'''
    특정 노드 -> 특정 노드 이런 문제는 다익스트라로 해결하면 되지만 
    모든 노드 -> 모든 노드 이런 문제는 플로이드 워셜 알고리즘으로 해결하면 된다.
    노드의 갯수가 최대 100개 이므로 O(n3) 까지도 가능하다.
    두 노드 사이의 간선이 여러개 일 수도 있으므로, 가장 비용이 적은 간선만 고려한다.
    플로이드 워셜
        점화식: graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        시간복잡도: O(n3)
    
'''


