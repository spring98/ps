
n = int(input())

answer = []
ordered_stack = []
results = []
no_flag = False

for i in range(1, n+1):
    ordered_stack.append(i)

for i in range(n):
    seq = int(input())
    while True:
        if not answer or answer[-1] < seq:
            answer.append(ordered_stack.pop(0))
            results.append('+')
        elif answer[-1] == seq:
            answer.pop()
            results.append('-')
            break
        else:
            no_flag = True
            break

if no_flag:
    print('NO')
else:
    for result in results:
        print(result)
'''
exit(0) 하면 바로 프로그램 종료시킬 수 있으니 
print('NO') 하고 프로그램 꺼버리면 됨.
03-stack 문제는 원하는 값이 나올 때 까지 while 로 넣거나 빼는 것이 특징
'''