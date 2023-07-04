import sys
input = sys.stdin.readline

sequence_num = int(input())
sequence_list = list(map(int, input().strip().split(' ')))
answer = []

no_flag = True
for i in range(sequence_num):
    for j in range(i+1, sequence_num):
        if sequence_list[i] < sequence_list[j]:
            answer.append(sequence_list[j])
            no_flag = False
            break
    if no_flag:
        answer.append(-1)
    no_flag = True

for item in answer:
    print(item, end=' ')


'''
11
3 2 1 10 9 5 4 8 15 11 13
10 10 10 15 15 8 8 15 -1 13 -1
time limit 걸림
'''
