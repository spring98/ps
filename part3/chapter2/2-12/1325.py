import heapq
import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().strip().split(' ')))

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = list(map(int, input().strip().split(' ')))
    graph[v].append(u)


def dfs(input_graph, start_node):
    visited = []
    need_visit = deque([start_node])

    while need_visit:
        node = need_visit.popleft()

        if node not in visited:
            visited.append(node)
            need_visit.extend(input_graph[node])

    return visited


# min_heap = []
# for i in range(1, N+1):
#     heapq.heappush(min_heap, (-len(dfs(graph, i)), i))
#
# ref_value = -1
# index_list = []
# while min_heap:
#     value, index = heapq.heappop(min_heap)
#     if ref_value <= -value:
#         ref_value = -value
#         index_list.append(index)
#     else:
#         break
#
# for index in index_list:
#     print(index, end=' ')

maxCnt = 1
ans = []

for i in range(1, N+1):
    cnt = len(dfs(graph, i))
    if cnt > maxCnt:
        maxCnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == maxCnt:
        ans.append(i)

print(*ans)

'''
    답은 맞는데 왜 time limit 걸리는 지 모르겠음
'''
