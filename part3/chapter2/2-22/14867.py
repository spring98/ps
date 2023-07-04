# limit_a, limit_b, target_a, target_b = 2, 5, 0, 1
# limit_a, limit_b, target_a, target_b = 3, 5, 2, 4
limit_a, limit_b, target_a, target_b = list(map(int, input().split(' ')))

def bfs(bottle_a, bottle_b):
    visited = []
    queue = []
    need_visit = [(bottle_a, bottle_b, 0)]

    while need_visit:
        node = need_visit.pop(0)
        a, b, w = node
        # print(f'a, b, w : {a, b, w}')

        if a == target_a and b == target_b:
            # print('finish')
            return w

        if (a, b) not in visited:
            # print(f'a, b, w : {a, b, w}')
            # a -> b 로 옮기기
            # a에 남아있는 물의 양이 b에 남아있는 빈공간 보다 적거나 같으면 모두 옮기기, 아니라면 b를 가득 채우고 나머지는 a가 가지고 있는다.
            empty_b = limit_b - b
            if a <= empty_b:
                a_to_b = (0, a+b, w+1)
            else:
                a_to_b = (a - empty_b, limit_b, w+1)

            empty_a = limit_a - a
            if b <= empty_a:
                b_to_a = (a + b, 0, w+1)
            else:
                b_to_a = (limit_a, b - empty_a, w+1)

            need_visit.extend([(limit_a, b, w+1), (a, limit_b, w+1), (0, b, w+1), (a, 0, w+1), a_to_b, b_to_a])
            visited.append((a, b))
            queue.append(node)

    return -1


print(bfs(0, 0))

