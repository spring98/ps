# import sys
# input = sys.stdin.readline
#
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#
#     if n == 1:
#         return 1
#
#     return fibonacci(n-2) + fibonacci(n-1)
#
# print(fibonacci(int(input().strip())))

'''
    재귀적으로 풀어서 time limit 발생
    해설은 matlab 에서 푸는 것 처럼 두 변수를 바꿔 더하면서 풀도록 했다.
'''

fibo = [0 for i in range(100)]

fibo[0] = 0
fibo[1] = 1

for i in range(0, 46):
    if i == 0:
        pass
    elif i == 1:
        pass
    else:
        fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[int(input().strip())])
