
test_case = int(input())

for _ in range(test_case):
    answer_array = []
    F = int(input())

    for _ in range(F):
        friend_a, friend_b = input().split(' ')

        if not answer_array:
            answer_array.append({friend_a, friend_b})
            print(2)

        else:
            temp_set = {friend_a, friend_b}
            for data in answer_array:
                if (friend_a in data) or (friend_b in data):
                    temp_set = temp_set | data
            answer_array.append(temp_set)
            print(len(temp_set))

'''
    time limit 걸림
    합집합 찾기(union find)
'''