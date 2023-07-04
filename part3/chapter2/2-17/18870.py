import sys
input = sys.stdin.readline

# N = int(input().strip())
# input_data = list(map(int, input().strip().split(' ')))
N = 5
input_data = [5, 2, 4, -10, 4, -9]

dp = [0] * 1000001
for data in input_data:
    dp[data] += 1

print(dp[:10])



# sorted_input_data = sorted(set(input_data), reverse=True)
# answers = []
#
# for data in input_data:
#     length = len(sorted_input_data)
#     index = sorted_input_data.index(data)
#     # answers.append(length - index - 1)
#     print(length - index - 1, end=' ')
#
# # for answer in answers:
# #     print(answer, end=' ')

'''
    아이디어는 맞았는데 (중복 제거 및 정렬, 인덱스 접근)
    list.index(data) 이게 문제였다. 
    for 문 안에 .index 를 수해하면 O(n2) 이 되기 때문..
    해설
    .index 를 하지 말고 오름차순으로 정렬한다음에 순서대로 0, 1, 2 이렇게 매핑해놓고 사용한다.
'''
