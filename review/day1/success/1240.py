# 4 2 -> 1000 으로 고정시키면 될 ㄷㅅ?
# 2 1 2
# 4 3 2
# 1 4 3
# 1 2
# 3 2

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(1001)]

for _ in range(N-1):
    u, v, w = list(map(int, input().split()))
    graph[u].append((v, w))
    graph[v].append((u, w))

# print(graph)


def bfs(input_graph, start_node, end_node):
    visited = []
    need_visit = deque([(start_node, 0)])

    while need_visit:
        node, weight = need_visit.popleft()

        if node == end_node:
            print(weight)
            break

        if node not in visited:
            for n, w in input_graph[node]:
                need_visit.append((n, w+weight))
            visited.append(node)

    return visited


for _ in range(M):
    query_start, query_end = map(int, input().split())
    bfs(graph, query_start, query_end)

