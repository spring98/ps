from itertools import permutations

N = int(input())
input_list = list(map(int, input().split()))

answer = 0
for permutation in permutations(input_list, N):
    tmp = 0
    for i in range(N-1):
        tmp += abs(permutation[i] - permutation[i+1])

    answer = max(answer, tmp)

print(answer)
