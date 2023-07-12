

# K, N = 1, 2
# input_data = [121]
#
K, N = list(map(int, input().split()))
input_data = []

for _ in range(K):
    input_data.append(int(input()))

def calculate(value):
    return_value = 0
    for data in input_data:
        return_value += (data // value)

    return return_value

start = 1
end = max(input_data)
mid = (start + end) // 2

answer = 0
count = 0

while True:
    calculated_value = calculate(mid)
    # print(mid, calculated_value)

    # if N == calculated_value:
    #     answer = mid
    #     break
    if N <= calculated_value:
        start = mid+1
        answer = mid
    else:
        end = mid-1

    mid = (start + end) // 2
    count += 1

    if count > 30:
        break


print(answer)
