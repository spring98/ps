
N = int(input())
input_data = list(map(int, input().split()))

sorted_data = sorted(input_data)

answer = 0
for i in range(N):
    for j in range(i+1):
        answer += sorted_data[j]
    #     print(j, end='')
    # print()

print(answer)
