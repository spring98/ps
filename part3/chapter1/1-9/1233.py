import sys
input = sys.stdin.readline

s1, s2, s3 = map(int, input().strip().split(' '))
answer = dict()

for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            dices_sum = i + j + k
            if answer.get(dices_sum) is None:
                answer[dices_sum] = 1
            else:
                answer[dices_sum] = answer.get(dices_sum)+1

answer_count = 0
answer_key = 0
for key in answer:
    count = answer.get(key)
    if answer_count < count:
        answer_count = count
        answer_key = key

print(answer_key)

