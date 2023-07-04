import sys
input = sys.stdin.readline


# 루트 왼쪽 오른쪽
def preorder(key):
    # 루트 출력
    print(key, end='')
    left = graph[key][0]
    right = graph[key][1]

    if left != '.':
        preorder(left)
    if right != '.':
        preorder(right)


# 왼쪽 루트 오른쪽
def inorder(key):
    left = graph[key][0]
    right = graph[key][1]

    if left != '.':
        inorder(left)
    # 루트 출력
    print(key, end='')
    if right != '.':
        inorder(right)


# 왼쪽 오른쪽 루트
def postorder(key):
    left = graph[key][0]
    right = graph[key][1]

    if left != '.':
        postorder(left)
    if right != '.':
        postorder(right)
    print(key, end='')


graph = {}
n = int(input().strip())

for _ in range(n):
    data, left, right = input().strip().split(' ')
    graph[data] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
