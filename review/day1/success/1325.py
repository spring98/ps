import heapq
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[v].append(u)


def bfs(input_graph, start_node):
    # visited = []
    count = 0
    visited = [0 for _ in range(N + 1)]
    need_visit = deque([start_node])

    while need_visit:
        node = need_visit.popleft()
        if not visited[node]:
            for n in input_graph[node]:
                need_visit.append(n)
            visited[node] = 1
            count += 1

    return count

answers = []

for i in range(1, N+1):
    # print(bfs(graph, i))
    heapq.heappush(answers, (-bfs(graph, i), i))

prev_max = -1
while answers:
    value, node = heapq.heappop(answers)
    if prev_max > -value:
        break
    prev_max = -value
    print(node, end=' ')


