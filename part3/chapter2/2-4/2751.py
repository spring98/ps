import sys
input = sys.stdin.readline

n = int(input().strip())

input_data = []
for _ in range(n):
    input_data.append(int(input().strip()))

input_data.sort()

for data in input_data:
    print(data)
