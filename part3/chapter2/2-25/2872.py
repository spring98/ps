# n = 4
# input_data = [3, 2, 1, 4]
# input_data = [1, 3, 4, 2]
# input_data = [3, 1, 2, 4]

import sys
input = sys.stdin.readline

n = int(input())
input_data = []

for _ in range(n):
    input_data.append(int(input()))

out_flag = True
count = 0
while True:
    # print(input_data)
    out_flag = True
    for i in range(n-1):
        max_value = input_data[i] - 1

        if max_value in input_data[i+1:]:
            input_data.remove(max_value)
            input_data.insert(0, max_value)
            count += 1
            out_flag = False

    if out_flag:
        break


# print(input_data)
print(count)

'''
    time out
    해설
    가장 큰 값(번호가 높은 책)은 옮길 필요가 없다.
    뒤에서 볼때 가장 큰 값부터 내림차순으로 구성된 원소들은 위치를 옮길 필요가 없다.
    따라서, 뒤에서 볼때 가장 큰 값부터 내림차순으로 구성된 원소의 개수를 구해서 N 에서 빼면 된다.
'''
