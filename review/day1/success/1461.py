# import sys
# input = sys.stdin.readline
#
# M, N = list(map(int, input().split()))
# input_data = list(map(int, input().split()))
# input_data.sort()
# # print(input_data)
#
# positives = []
# negatives = []
#
# for data in input_data:
#     if data > 0:
#         positives.append(data)
#     else:
#         negatives.append(-data)
#
# # print(positives)
# # print(negatives)
#
# first_value = 0
# if (not positives) and negatives:
#     first_value = max(negatives)
# elif positives and (not negatives):
#     first_value = max(positives)
# else:
#     if max(positives) > max(negatives):
#         first_value = max(positives)
#     else:
#         first_value = max(negatives)
#
# count = 0
# while negatives or positives:
#     if negatives and positives:
#         # print(f'p: {positives}, n: {negatives}')
#         if max(negatives) < max(positives):
#             count += (positives[-1] * 2)
#             for _ in range(N):
#                 if positives:
#                     positives.pop()
#
#         elif max(negatives) > max(positives):
#             count += (negatives[0] * 2)
#             for _ in range(N):
#                 if negatives:
#                     negatives.pop(0)
#
#     else:
#         while positives:
#             count += (positives[-1] * 2)
#             for _ in range(N):
#                 if positives:
#                     positives.pop()
#
#         while negatives:
#             count += (negatives[0] * 2)
#             for _ in range(N):
#                 if negatives:
#                     negatives.pop(0)
#
#
# print(count-first_value)
#

'''
import sys
input = sys.stdin.readline

M, N = list(map(int, input().split()))
input_data = list(map(int, input().split()))
input_data.sort()
# print(input_data)

positives = []
negatives = []

for data in input_data:
    if data > 0:
        positives.append(data)
    else:
        negatives.append(-data)

# print(positives)
# print(negatives)

first_value = 0
if (not positives) and negatives:
    first_value = max(negatives)
elif positives and (not negatives):
    first_value = max(positives)
else:
    if max(positives) > max(negatives):
        first_value = max(positives)
    else:
        first_value = max(negatives)

count = 0
while negatives or positives:
    if negatives and positives:
        # print(f'p: {positives}, n: {negatives}')
        if max(negatives) < max(positives):
            count += (positives[-1] * 2)
            for _ in range(N):
                if positives:
                    positives.pop()

        elif max(negatives) > max(positives):
            count += (negatives[0] * 2)
            for _ in range(N):
                if negatives:
                    negatives.pop(0)

    else:
        while positives:
            count += (positives[-1] * 2)
            for _ in range(N):
                if positives:
                    positives.pop()

        while negatives:
            count += (negatives[0] * 2)
            for _ in range(N):
                if negatives:
                    negatives.pop(0)


print(count-first_value)
'''
