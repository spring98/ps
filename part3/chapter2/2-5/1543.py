import sys
input = sys.stdin.readline

input_data = input().strip()
target = input().strip()
count = 0

while input_data.find(target) != -1:
    index = input_data.find(target)
    input_data = input_data[index+len(target):]
    count += 1

print(count)

