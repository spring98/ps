input_data = 1000 - int(input())

targets = [500, 100, 50, 10, 5, 1]
count = 0
for target in targets:
    while target <= input_data:
        input_data = input_data - target
        count += 1

print(count)
