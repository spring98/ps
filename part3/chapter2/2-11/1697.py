
count = 0
array = [0] * 100001

def bfs(start_node):
    global count
    visited = []
    need_visit = [start_node]

    while need_visit:
        node = need_visit.pop(0)

        if node == 17:
            break
        count += 1

        if node not in visited:
            visited.append(node)
            need_visit.extend([node-1, node+1, node*2])

    print(f'need : {need_visit}')

    return visited


visited_bfs = bfs(5)
print(f'visited count : {len(visited_bfs)}')

# for bfs in visited_bfs:
#     print(bfs, end=' ')

print(f'{count}')

'''
    array 를 하나 추가하여 레벨을 저장해야 한다.
    그리고 내가 한 것처럼 뽑은 노드가 visited 에 없을 때 3가지를 추가하는 것이 아니라
    for 문으로 3가지를 후보로 가지고 visited 가 아니라면 need_visit 에 추가하는 방식으로 해야한다. 
    이때 추가할때 array 를 사용하여 지금 레벨값 + 1 을 3개 후보를 추가할때 array에 대입한다.
'''