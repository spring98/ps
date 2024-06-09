def solution(n, m, x, y, r, c, k):
    answers = []
    x_length = m
    y_length = n
    start_x, start_y = y-1, x-1
    end_x, end_y = c-1, r-1

    miro = [[0 for _ in range(x_length)] for _ in range(y_length)]
    miro[start_y][start_x] = 'S'
    miro[end_y][end_x] = 'E'

    visited = []
    flag = False

    def dfs(local_x, local_y, path=''):
        nonlocal flag
        x, y, path = local_x, local_y, path
        print(path)
        if x == end_x and y == end_y and len(path) == k:
            print(path)
            answers.append(path)
            flag = True

        if flag or k < len(path):
            return

        # if (x, y) not in visited and 0 <= x < x_length and 0 <= y < y_length:
        if 0 <= x < x_length and 0 <= y < y_length:
            visited.append((x, y))
            dfs(x, y+1, path+'d')
            dfs(x-1, y, path+'l')
            dfs(x+1, y, path+'r')
            dfs(x, y-1, path+'u')
            visited.remove((x, y))

    dfs(start_x, start_y)

    if answers:
        return sorted(answers)[0]

    else:
        return 'impossible'

# def solution(n, m, x, y, r, c, k):
#     lrud = {0: 'd', 1: 'l', 2: 'r', 3: 'u'}
#     dx = [1, 0, 0, -1]
#     dy = [0, -1, 1, 0]
#     answer = 'impossible'
#     flag = False
#     stack = []
#
#     def DFS(X, Y, L):
#         nonlocal answer, flag
#         if flag or k < L + abs(X - r) + abs(Y - c):
#             return
#         if L == k and (X, Y) == (r, c):
#             answer = ''.join(stack)
#             flag = True
#         else:
#             for i in range(4):
#                 nX = X + dx[i]
#                 nY = Y + dy[i]
#                 if 1 <= nX <= n and 1 <= nY <= m:
#                     stack.append(lrud[i])
#                     DFS(nX, nY, L+1)
#                     stack.pop()
#
#     dist = abs(x - r) + abs(y - c)
#     if dist <= k and (k - dist) % 2 == 0:
#         DFS(x, y, 0)
#     return answer


print(f'result: {solution(3,4,2,3,3,1,5)}')
# print(f'result: {solution(2,2,1,1,2,2,2)}')
# print(f'result: {solution(3,3,1,2,3,3,4)}')
