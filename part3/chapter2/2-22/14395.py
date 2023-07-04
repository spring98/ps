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

        if node not in visited:
            need_visit.extend([(node * 2, weight + 1), (int(str(node) + '1'), weight + 1)])
            visited.append(node)

    return -1


print(bfs(A, B))

'''
    최단경로의 weight 뿐만 아니라 경로도 구하고 싶다면 (node, weight, path) 이렇게 추가하면서 bfs를 계속 진행하면 된다.
'''