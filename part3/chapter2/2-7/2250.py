import sys
input = sys.stdin.readline
import heapq


graph = {}
n = int(input().strip())

for _ in range(n):
    data, left, right = map(int, input().strip().split(' '))
    graph[data] = [left, right]

coord_data = []

y = 1
x = 0


# 왼쪽 루트 오른쪽
def inorder(key):
    global y, x

    left = graph[key][0]
    right = graph[key][1]

    if left != -1:
        y += 1
        inorder(left)
    # 루트 출력
    x += 1
    # print(f'{key}:({x}, {y})', end=' ')
    heapq.heappush(coord_data, (y, x))
    if right != -1:
        y += 1
        inorder(right)

    y -= 1

inorder(1)


prev_key = 1
current_data = []
answer = []
# print()
while coord_data:
    key, data = heapq.heappop(coord_data)
    if prev_key == key:
        current_data.append(data)

    # 새로운 키의 등장
    else:
        heapq.heappush(answer, (-(max(current_data)-min(current_data)+1), prev_key))
        # answer.append((prev_key, max(current_data)-min(current_data)+1))
        current_data = []
        prev_key = key
        current_data.append(data)

# print(answer)
width, key = heapq.heappop(answer)
print(f'{key} {-width}')

'''
    방향은 맞았으나 1이 항상 루트가 되는 것이 아님을 고려하지 않았다.
    루트를 구하기 위해서 parent 변수를 둬서 초기화 할 당시에 부모를 기록해놓고
    나중에 한번더 순회를 하고 그때 부모가 없는 노드를 찾아 그것이 루트임을 확인해야 한다. 
'''