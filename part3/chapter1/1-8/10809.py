alphabet = dict()
for i, alpha in enumerate('abcdefghijklmnopqrstuvwxyz'):
    alphabet[alpha] = i

answer = [-1] * 26

input_data = list(dict.fromkeys(input().strip()))

for i, spell in enumerate(input_data):
    answer[alphabet[spell]] = i

print(answer)

