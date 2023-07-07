# graph = [
#     [],  # 0
#     [2, 3],  # 1
#     [7, 8, 9, 1],  # 2
#     [1],  # 3
#     [5, 6],  # 4
#     [4],  # 5
#     [4],  # 6
#     [2],  # 7
#     [2],  # 8
#     [2],  # 9
# ]

graph = [[] for _ in range(101)]

N = int(input())
target_x, target_y = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
# print(graph)

def bfs():
    visited = []
    need_visit = []
    for n in graph[target_x]:
        need_visit.append((n, 1))

    while need_visit:
        node, weight = need_visit.pop(0)

        if node == target_y:
            print(weight)
            quit()

        if node not in visited:
            visited.append(node)
            for n in graph[node]:
                need_visit.append((n, weight+1))

    print(-1)
    quit()


bfs()

