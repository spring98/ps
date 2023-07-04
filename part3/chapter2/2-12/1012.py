# input_data = [
#     (0, 0), (1, 0), (1, 1), (4, 2), (4, 3), (4, 5), (2, 4), (3, 4), (7, 4), (8, 4), (9, 4), (7, 5),
#     (8, 5), (9, 5), (7, 6), (8, 6), (9, 6)
# ]
# for data in input_data:
#     x, y = data
#     one_dim_map[x + 10*y] = 1
#     dim_list.append(x + 10*y)

import sys
input = sys.stdin.readline

test_case = int(input().strip())
for _ in range(test_case):

    M, N, K = list(map(int, input().strip().split(' ')))
    dim_list = []

    for _ in range(K):
        x, y = list(map(int, input().strip().split(' ')))
        dim_list.append(x + M*y)


    def dfs(start_node):
        visited = []
        need_visit = [start_node]

        while need_visit:
            node = need_visit.pop()

            for target in (node-1, node+1, node-M, node+M):
                if node not in visited and target in dim_list:
                    need_visit.extend([target])
                    dim_list.pop(dim_list.index(target))
            visited.append(node)

        return visited


    answer = []
    # print(dim_list)

    while dim_list:
        answer.append(dfs(dim_list.pop()))

    # print(answer)
    print(len(answer))

'''
    푼거같은데 틀림;
    해설
    모든 정점에 대해서 dfs 혹은 bfs 를 적용한다. 
    배추가 없는 곳, 그리고 이미 적용한 곳은 dfs, bfs 를 하지 않는다.
    dfs, bfs 를 수행한 횟수를 세면 된다.
    visited 와 땅 정보를 둘다 2차원 배열로 설정해서 문제를 해결한다.
'''
