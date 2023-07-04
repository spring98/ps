import heapq

n = 8
graph = [
    [1, 1, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 1],
]


def bfs(input_graph, input_x, input_y):
    visited = []
    need_visit = []
    heapq.heappush(need_visit, (0, input_x, input_y))

    while need_visit:
        w, x, y = heapq.heappop(need_visit)

        if (x, y) not in visited:
            if (x == (n - 1)) and (y == (n - 1)):
                print('finished')

            if 0 <= x < n and 0 <= y < n:
                if input_graph[y][x] == 1:
                    dw = 0
                else:
                    dw = 1
                heapq.heappush(need_visit, (w+dw, x+1, y))
                heapq.heappush(need_visit, (w+dw, x, y+1))
                heapq.heappush(need_visit, (w+dw, x-1, y))
                heapq.heappush(need_visit, (w+dw, x, y-1))

                visited.append((x, y))
                print(f'x, y, w : {x + 1, y + 1, w}')

    return visited


bfs(graph, 0, 0)

'''
    대강 아이디어는 맞았는데 결정적인 아이디어를 놓쳤다.
    bfs 를 queue 로 구현했었으나 여기서는 검은방을 지나친 것을 기준으로 큐에 넣어야 하기 때문에 
    튜블내에 weight 를 맨 앞에 두고 min_heap 을 이용하여 weight 가 가장 작은 놈이 먼저 탐색하게 만들어야 한다.
'''