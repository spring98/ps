import sys
input = sys.stdin.readline

y, x = map(int, input().strip().split(' '))

input_data = []

for _ in range(y):
    input_data.append(input().strip())

count = 0
for data in input_data:
    if data.find('X') == -1:
        count += 1

print(count)

'''
    wrong answer
    나는 가로 부분에 대해서만 경비가 없을때 카운트 햇지만
    세로부분에 대해서도 경비가 없을 때 카운트를 해서 둘중에 큰 값을 사용해야 한다.
'''