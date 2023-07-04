
N = int(input())
input_data = list(map(int, input().split(' ')))

data_dict = {}
for data in input_data:
    data_dict[data] = True

M = int(input())
test_data = list(map(int, input().split(' ')))

for data in test_data:
    if data in data_dict:
        print(1)
    else:
        print(0)
