import sys
input = sys.stdin.readline

test_case = int(input())
stack = [1]
answer = ['+']
no_flag = False
input_count = 2

for _ in range(test_case):
    input_data = int(input())
    while True:
        if stack:
            if stack[-1] > input_data:
                stack.pop()
                answer.append('-')

            elif stack[-1] < input_data:
                stack.append(input_count)
                answer.append('+')

            elif stack[-1] == input_data:
                stack.pop()
                answer.append('-')
                break

            input_count += 1

        else:
            no_flag = True
            break

if no_flag:
    print('NO')
else:
    for a in answer:
        print(a)
