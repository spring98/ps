import sys
input = sys.stdin.readline

N = int(input())
input_data = []

for _ in range(N):
    x, y = map(int, input().split())
    input_data.append((x, y))

input_data.sort()

# print(input_data)

answer = 0

prev_start, prev_end = input_data[0]
# answer += (prev_end - prev_start)

for curr_start, curr_end in input_data[1:]:

    # print(prev_start, prev_end)
    if curr_start <= prev_end < curr_end:
        # answer += (curr_end - prev_end)
        prev_end = curr_end

    if prev_end < curr_start:
        # answer += (curr_end - curr_start)
        answer += (prev_end - prev_start)
        prev_start = curr_start
        prev_end = curr_end

answer += (prev_end - prev_start)
print(answer)
