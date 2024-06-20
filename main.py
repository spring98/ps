import heapq, math

# def count_divisors_sqrt(n):
#     count = 0
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             if i == n // i:
#                 count += 1  # i와 n//i가 같은 경우 (완전 제곱수)
#             else:
#                 count += 2  # i와 n//i가 다른 경우
#     return count

def solution(e, starts):
    answers = []
    myStarts = []

    for i, start in enumerate(starts):
        myStarts.append((start, i))

    myStarts.sort()

    table = [0] * (e + 1)
    for i in range(2, e + 1):
        for j in range(1, min(e // i + 1, i)):
            table[i * j] += 2
    for i in range(1, int(e ** (1 / 2)) + 1):
        table[i ** 2] += 1

    # table = [-1]
    # for n in range(1, e+1):
    #     table.append(count_divisors_sqrt(n))

    # print(table)
    myHeap = []
    for i, t in enumerate(table):
        heapq.heappush(myHeap, (-t, i))

    for start, priority in myStarts:
        while myHeap:
            value, index = heapq.heappop(myHeap)

            if start <= index:
                answers.append((priority, index))
                heapq.heappush(myHeap, (value, index))
                break

    answers.sort()
    # print(answers)
    re = []
    for p, value in answers:
        re.append(value)

    return re

# print(f'result: {solution(8,[1,3,7])}')
print(f'result: {solution(8,[7,3,1])}')
# print(f'result: {solution(15,[7,8])}')
# print(f'result: {solution(11,[6,8])}')
# print(f'result: {solution(1000,[])}')


