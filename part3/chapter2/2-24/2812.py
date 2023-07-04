input_data = [4, 1, 7, 7, 2, 5, 2, 8, 4, 1]

temp_data = []



for _ in range(4):
    a = input_data.pop(0)
    b = input_data.pop(0)

    if a >= b:
        temp_data.append(a)
        a = b
    else:
        input_data.insert(0, b)
        while temp_data:
            input_data.insert(0, temp_data.pop())


    print(input_data)


'''
    해설
    1. input으로 받은 원소를 차례대로 하나씩 확인한다. 
    2. 현재의 원소가 스택의 Top 보다 크면, 작을 때 까지 스택에서 Pop 한다.
    3. 현재 원소를 스택에 삽입한다.
'''