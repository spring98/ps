
test_case = int(input())

for i in range(test_case):

    data_list = list(input())
    answer = []
    temp = []

    for data in data_list:
        if data == '<':
            if not answer:
                pass
            else:
                top = answer.pop()
                temp.append(top)

        elif data == '>':
            if not temp:
                pass
            else:
                top = temp.pop()
                answer.append(top)

        elif data == '-':
            if not answer:
                pass
            else:
                answer.pop()

        else:
            answer.append(data)

    while True:
        if temp:
            answer.append(temp.pop())
        else:
            break

    print(''.join(answer))


'''
    들으려고 한건 아니지만 힌트를 받아버리고 시작함 ,, 
'''