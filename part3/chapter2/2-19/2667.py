#
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# house_map = [
#     [0, 1, 1, 0, 1, 0, 0],
#     [0, 1, 1, 0, 1, 0, 1],
#     [1, 1, 1, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0, 0, 0],
# ]
import sys
input = sys.stdin.readline

N = int(input().strip())
house_map = [[] for _ in range(N)]
for i in range(N):
    rows = input().strip()
    for row in rows:
        house_map[i].append(int(row))

# print(house_map)
visited = []


def dfs(input_map, cur_x, cur_y):
    global visited
    local_visited = []
    need_visited = [(cur_x, cur_y)]

    while need_visited:
        coord = need_visited.pop()
        x, y = coord
        if coord not in visited:
            if 0 <= x < N and 0 <= y < N and input_map[x][y] == 1:
                need_visited.extend([(x+1, y), (x, y+1), (x-1, y), (x, y-1)])
                visited.append(coord)
                local_visited.append(coord)

    return local_visited


answers = []
for i in range(N):
    for j in range(N):
        visit_list = dfs(house_map, i, j)
        if visit_list:
            answers.append(len(visit_list))

answers.sort()
print(len(answers))
for answer in answers:
    print(answer)

