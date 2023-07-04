# import sys
# input = sys.stdin.readline
#
# def dfs(index):
#     if visited[index]:
#         return
#     print(index)
#
#     for i in range(1, len(graph[index])+1):
#         visited[index] = True
#         dfs(graph[index])
#
#
#
# N, M = map(int, input().strip().split(' '))
#
# graph = [[0] for _ in range(N+1)]
# visited = [False] * (N+1)
#
# for _ in range(M):
#     u, v = map(int, input().strip().split(' '))
#     graph[u].append(v)
#     graph[v].append(u)
#
# dfs(1)





