import sys
input = sys.stdin.readline

N = int(input().strip())
input_datas = []
for _ in range(N):
    input_datas.append(input().strip())

answers = []

for datas in input_datas:
    first = len(datas)
    second = 0

    for data in datas:
        if data.isdigit():
            second += int(data)

    answers.append((first, second, datas))

sorted_answer = sorted(answers)

for answer in sorted_answer:
    print(answer[2])



