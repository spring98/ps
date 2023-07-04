import sys
input = sys.stdin.readline

n = int(input().strip())

answer = []
for _ in range(n):
    value = int(input().strip())
    answer.append(value)

for item in sorted(answer):
    print(item)
