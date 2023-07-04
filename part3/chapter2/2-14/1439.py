
input_data = input()
prev = ''
answer_list = []
for data in input_data:
    if prev != data:
        answer_list.append(data)
        prev = data

zero_count = 0
one_count = 0

for answer in answer_list:
    if answer == '0':
        zero_count += 1
    elif answer == '1':
        one_count += 1

if zero_count < one_count:
    print(zero_count)
elif zero_count > one_count:
    print(one_count)
else:
    print(zero_count)

