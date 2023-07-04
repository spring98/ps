import sys
input = sys.stdin.readline

input_data = []

for i in range(5):
    score = list(map(int, input().strip().split(' ')))
    input_data.append((sum(score), i+1))


number, score = max(input_data)[1], max(input_data)[0]

print(f'{number} {score}')



