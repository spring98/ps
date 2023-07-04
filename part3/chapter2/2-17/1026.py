import sys
input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().strip().split(' ')))
B_list = list(map(int, input().strip().split(' ')))

A_list.sort()
B_list.sort()

answer = 0
for A in A_list:
    answer += A * B_list.pop()

print(answer)