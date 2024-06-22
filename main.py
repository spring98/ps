def solution(numbers):
    graph = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
    index_table = [(1, 3), (0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    dx = [1, 0, -1, 0, 1, -1, 1, -1]
    dy = [0, 1, 0, -1, 1, 1, -1, -1]
    # dd = ['r', 'd', 'l', 'u', 'di', 'di', 'di', 'di']
    dd = [2, 2, 2, 2, 3, 3, 3, 3]

    def bfs(start_num, end_num):
        start_x, start_y = index_table[start_num]
        end_x, end_y = index_table[end_num]
        # need_visit = [(start_x, start_y, [])]
        need_visit = [(start_x, start_y, 0)]
        visited = []

        while need_visit:
            x, y, p = need_visit.pop(0)
            # print(x, y, p)

            if x == end_x and y == end_y:
                if not p:
                    return 1
                return p

            visited.append((x, y))

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                nd = dd[i]

                if (nx, ny) not in visited and 0 <= nx < 3 and 0 <= ny < 4 and graph[ny][nx] != -1:
                    # need_visit.append((nx, ny, p+[nd]))
                    need_visit.append((nx, ny, p+nd))

    dp = [[[0, 0] for _ in range(2)] for _ in range(len(numbers)+1)]
    dp[0][0] = [0, 4]
    dp[0][1] = [0, 6]
    # print(dp)

    for i, number in enumerate(numbers):
        number = int(number)

        if i > 0:
            if dp[i][0] == [0, 0]:
                # dp[i][0] = copy.deepcopy(dp[i-1][0])
                dp[i][0] = dp[i-1][0]

            if dp[i][1] == [0, 0]:
                dp[i][1] = dp[i-1][1]

        # 왼손에서 출발
        left = bfs(dp[i][0][1], number)

        # 오른손에서 출발
        right = bfs(dp[i][1][1], number)

        # 더 작은 값을 가진 쪽에 최종 점수 추가하고 현재위치 업데이트
        if left < right:
            dp[i][0][0] += left
            dp[i][0][1] = number

        else:
            dp[i][1][0] += right
            dp[i][1][1] = number

    # print(dp)
    return dp[len(numbers)-1][0][0] + dp[len(numbers)-1][1][0]

# print(f'result: {solution("1756")}')
print(f'result: {solution("5123")}')


