from collections import deque

N, K = map(int, input().split())


def bfs(start_node):
    visited = [0 for _ in range(100001)]
    need_visited = deque([(start_node, 0)])

    while need_visited:
        node, weight = need_visited.popleft()
        if node > 100000:
            continue

        if node == K:
            print(weight)
            break
        if visited[node] == 0:
            a = node - 1
            b = node + 1
            c = node * 2
            if 0 <= a <= 100000:
                need_visited.append((a, weight+1))
            if 0 <= b <= 100000:
                need_visited.append((b, weight + 1))
            if 0 <= c <= 100000:
                need_visited.append((c, weight + 1))

            visited[node] = 1

    return visited


bfs(N)
