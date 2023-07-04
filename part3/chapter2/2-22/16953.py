from collections import deque
import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split(' '))


def bfs(start_node, end_node):
    visited = []
    need_visit = deque([(start_node, 1)])

    while need_visit:
        tup = need_visit.popleft()
        node, weight = tup

        if end_node < node:
            continue

        if node == end_node:
            return weight

        # if need_visit and (min(need_visit)[0] > end_node):
        #     return -1

        if node not in visited:
            need_visit.extend([(node * 2, weight + 1), (int(str(node) + '1'), weight + 1)])
            visited.append(node)

    return -1


print(bfs(A, B))
