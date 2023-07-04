N = int(input())

sum_value = 0
count = 0
target_value = 1
while True:
    if sum_value > N:
        break
    if target_value < N:
        target_value = 1

    sum_value += target_value
    target_value += 1
    count += 1

print(count)
