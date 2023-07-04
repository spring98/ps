# clear


import sys
input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):

    x_count, y_count, K = list(map(int, input().split()))

    # map 을 생성할 때는 x와 y를 반대로 생성해야 [x][y]로 접근할 수 있다.
    cabbage_map = [[0] * y_count for _ in range(x_count)]

    for _ in range(K):
        ix, iy = list(map(int, input().split()))
        cabbage_map[ix][iy] = 1


    # for i in range(y_count):
    #     for j in range(x_count):
    #         print(cabbage_map[j][i], end=' ')
    #     print()

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = []
    answer = 0


    def bfs(current_x, current_y):
        global answer
        need_visit = [(current_x, current_y)]
        local_visited = []

        while need_visit:
            x, y = need_visit.pop(0)
            for index in range(4):
                nx = x + dx[index]
                ny = y + dy[index]
                if (0 <= nx < x_count) and (0 <= ny < y_count) and ((nx, ny) not in visited and (cabbage_map[nx][ny] == 1)):
                    need_visit.append((nx, ny))
                    visited.append((nx, ny))
                    local_visited.append((nx, ny))

        # if local_visited:
        #     print(local_visited)
        #     answer += 1


    for i in range(x_count):
        for j in range(y_count):
            if cabbage_map[i][j] and (i, j) not in visited:
                bfs(i, j)
                answer += 1

    print(answer)

