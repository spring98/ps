# N = 5
# rbg_map = [
#     ['R', 'R', 'R', 'B', 'B'],
#     ['G', 'G', 'B', 'B', 'B'],
#     ['B', 'B', 'B', 'R', 'R'],
#     ['B', 'B', 'R', 'R', 'R'],
#     ['R', 'R', 'R', 'R', 'R'],
# ]

import sys
input = sys.stdin.readline

N = int(input().strip())
rbg_map = [[] for _ in range(N)]
for i in range(N):
    rows = input().strip()
    for row in rows:
        rbg_map[i].append(row)

# print(rbg_map)
visited = []


def dfs(input_map, current_x, current_y, color, challenged=''):
    local_visited = []
    need_visit = [(current_x, current_y)]

    while need_visit:
        node = need_visit.pop()
        x, y = node
        if node not in visited:
            if 0 <= x < N and 0 <= y < N and (input_map[x][y] == color or input_map[x][y] == challenged):
                need_visit.extend([(x+1, y), (x, y+1), (x-1, y), (x, y-1)])
                visited.append(node)
                local_visited.append(node)

    return local_visited


answer_general = []
answer_challenged = []

# 일반인
for i in range(N):
    for j in range(N):
        result_r = dfs(rbg_map, i, j, 'R')
        if result_r:
            # print(result_r)
            answer_general.append(result_r)

        result_g = dfs(rbg_map, i, j, 'G')
        if result_g:
            # print(result_g)
            answer_general.append(result_g)

        result_b = dfs(rbg_map, i, j, 'B')
        if result_b:
            # print(result_b)
            answer_general.append(result_b)

# print()
visited = []
# 정록색약
for i in range(N):
    for j in range(N):
        result_rg = dfs(rbg_map, i, j, 'R', 'G')
        if result_rg:
            # print(result_rg)
            answer_challenged.append(result_rg)

        result_b = dfs(rbg_map, i, j, 'B')
        if result_b:
            # print(result_b)
            answer_challenged.append(result_b)

print(len(answer_general), end=' ')
print(len(answer_challenged))
