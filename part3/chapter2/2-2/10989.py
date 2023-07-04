# import sys
# input = sys.stdin.readline
#
# input_data = []
#
# n = int(input().strip())
# for _ in range(n):
#     data = int(input().strip())
#     input_data.append(data)
#
# sorted_data = sorted(input_data)
#
# for _ in sorted_data:
#     print(_)

'''
    메모리 초과, time limit 도 같이 걸렸을 것이다. 
    데이터의 양이 1000만개 이므로 O(n) 에 풀어야 한다.
    데이터의 양이 많은 대신 데이터의 값은 10000이하이므로 작다.
    이럴 때 계수정렬을 이용하면 O(n) 에 해결할 수 있다.
'''
import sys
input = sys.stdin.readline

counting_table = [0] * 10001

n = int(input().strip())
for _ in range(n):
    data = int(input().strip())
    counting_table[data] += 1

for i, data in enumerate(counting_table):
    if counting_table[i] == 0:
        pass
    else:
        count = counting_table[i]
        for _ in range(count):
            print(i)










