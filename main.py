from itertools import product

def solution(user_id, banned_id):
    answers = set()
    myMap = {}

    for id, ban in enumerate(banned_id):
        for user in user_id:
            isCorrect = True
            if len(ban) == len(user):
                for i in range(len(ban)):
                    if ban[i] != '*' and user[i] != ban[i]:
                        isCorrect = False
            else:
                isCorrect = False

            key = f'{id}_{ban}'
            if isCorrect:
                if key in myMap:
                    myMap[key].append(user)
                else:
                    myMap[key] = [user]

    # print(myMap)
    values = myMap.values()

    for result in product(*list(values)):
        if len(result) == len(set(result)):
            answers.add(''.join(sorted(result)))

    return len(answers)

print(f'result: {solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])}')
print(f'result: {solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])}')
print(f'result: {solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])}')
# print(f'result: {solution(["frodo"], ["*****"])}')

