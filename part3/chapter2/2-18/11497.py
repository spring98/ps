
N = 5
input_data = [2, 4, 5, 7, 9]
input_data.sort()

rights = []
lefts = []

center = input_data.pop(0)
rights.append(center)
lefts.append(center)

while input_data:
    first = input_data.pop(0)
    second = input_data.pop(0)

    left = lefts[-1]
    right = rights[-1]

    temp = [(first-left, 0), (first-right, 1), (second-left, 2), (second-right, 3)]

    print(max(temp))

    if max(temp)[1] == 0:
        rights.append(first)
        lefts.append(second)
    elif max(temp)[1] == 1:
        rights.append(second)
        lefts.append(first)
    elif max(temp)[1] == 2:
        rights.append(second)
        lefts.append(first)
    elif max(temp)[1] == 3:
        rights.append(first)
        lefts.append(second)

    print(temp)

'''
    음.. 내가 너무 꼬아서 생각한 것 같다.
    그냥 순서대로 왼쪽 오른쪽 왼쪽 오른쪽 반복해서 넣어버린면 된다... ㅠㅠ
'''
