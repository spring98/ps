from collections import deque

# list = deque()
# list.popleft()

# max_height, start, end, up, down = 100, 2, 1, 1, 0
# max_height, start, end, up, down = 10, 1, 10, 2, 1
max_height, start, end, up, down = list(map(int, input().split()))

visited = [False for _ in range(max_height+1)]
global_weight = 0
def bfs(start_node):

    global global_weight
    need_visit = deque([(start_node, 0)])

    while need_visit:
        node, weight = need_visit.popleft()
        global_weight = weight
        # print(node, weight)

        if node == end:
            print(weight)
            return

        for next_node in (node+up, node-down):
            if 1 <= next_node <= max_height and not visited[next_node]:
                need_visit.append((next_node, weight+1))
                visited[next_node] = True

    if not visited[end]:
        print('use the stairs')


# 10 1 10 2 1
bfs(start)


