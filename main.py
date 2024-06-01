def solution(board):
    n = len(board)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    all_paths = []

    def dfs(x, y, path):
        path.append((x, y))

        if x == n - 1 and y == n - 1:
            all_paths.append(path.copy())
            path.pop()
            print(path)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in path and board[ny][nx] == 0:
                dfs(nx, ny, path)

        path.pop()

    dfs(0, 0, [])

    print(all_paths)

    costs = []
    for paths in all_paths:
        prev = ''
        cost = 0
        for i in range(len(paths)-1):
            startX, startY = paths[i]
            endX, endY = paths[i+1]
            curr = ''

            if abs(endX - startX) == 1:
                curr = 'H'

            if abs(endY - startY) == 1:
                curr = 'V'

            if curr == 'H' and prev == 'V' or curr == 'V' and prev == 'H':
                cost += 500

            cost += 100
            prev = curr

        costs.append(cost)

    return min(costs)

# print(f'result: {solution([[0,0,0],[0,0,0],[0,0,0]])}')
print(f'result: {solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])}')
# print(f'result: {solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])}')
# print(f'result: {solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])}')

