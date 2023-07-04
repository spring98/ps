import sys
input = sys.stdin.readline

test_case = int(input())
answer_stack = []

for _ in range(test_case):
    command = input().strip().split(' ')

    if command[0] == 'push':
        answer_stack.append(int(command[1]))
    elif command[0] == 'pop':
        if not answer_stack:
            print(-1)
        else:
            print(answer_stack.pop())
    elif command[0] == 'size':
        print(len(answer_stack))
    elif command[0] == 'empty':
        if not answer_stack:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if not answer_stack:
            print(-1)
        else:
            print(answer_stack[-1])
