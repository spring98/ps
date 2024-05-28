
from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = list(map(int, input().split()))

distance = [300001] * (300001)
visited = [False] * (300001)
graph = [[] for _ in range((300001))]

for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)

def bfs(start_node):
    need_visit = deque([(start_node, 0)])

    while need_visit:
        node, weight = need_visit.popleft()
        distance[node] = min(distance[node], weight)
        # print(f'node, weight : {node, weight}')

        if not visited[node]:
            visited[node] = True
            # print(node)
            for item in graph[node]:
                need_visit.append((item, weight+1))

bfs(X)

# print(distance)

found_flag = False
for index, value in enumerate(distance):
    if value == K:
        found_flag = True
        print(index)

if not found_flag:
    print(-1)
