
n, w, L = list(map(int, input().split()))
trucks = list(map(int, input().split()))

answer = []

for i in range(n):
    weight_sum = 0
    for j in range(i, i+w):
        if len(trucks)-1 < j:
            break
        weight = trucks[j]

        if weight_sum + weight <= L:
            weight_sum += weight
            answer.append(weight)
        else:
            answer.append(0)

print(answer)

if answer[-1] != 0:
    print(len(answer)+w-1)
