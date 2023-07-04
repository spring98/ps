# 실버 2

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [0] * (N+1)
def bfs(start_node):
    local_visit = []
    need_visit = deque()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.popleft()
        if visited[node] == 0:
            need_visit.extend(graph[node])
            visited[node] = 1
            local_visit.append(node)

    return local_visit


answer = 0
for i in range(1, N+1):
    if len(bfs(i)) > 0:
        answer += 1

print(answer)
