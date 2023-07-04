# [실패]
import sys
input = sys.stdin.readline

input_data = 11

count_5kg_first = input_data // 5
rest_first = input_data % 5

count_3kg_first = rest_first // 3
rest_first = rest_first % 3


count_3kg_second = input_data // 3
rest_second = input_data % 3

count_5kg_second = rest_second // 5
rest_second = rest_second % 5


sum_fist = count_3kg_first + count_5kg_first
sum_second = count_3kg_second + count_5kg_second
if rest_first != 0 and rest_second != 0:
    print('-1')
else:
    if sum_fist > sum_second:
        if rest_second == 0:
            print(sum_second)
        else:
            print(sum_fist)

    elif sum_fist < sum_second:
        if rest_first == 0:
            print(sum_fist)
        else:
            print(sum_second)
    else:
        print(-1)


