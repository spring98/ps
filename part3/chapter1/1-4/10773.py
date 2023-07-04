import sys
input = sys.stdin.readline

test_case = int(input().strip())

answer_stack = []
for _ in range(test_case):
    n = int(input().strip())
    if n == 0:
        answer_stack.pop()
    else:
        answer_stack.append(n)

answer_sum = 0
for item in answer_stack:
    answer_sum += item

print(answer_sum)
