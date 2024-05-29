def solution(stones, k):
    answer = 0
    zeros = []
    base = 0

    for _ in range(len(set(stones))):
        minValue = min(stones)
        local_zeros = []
        for i in range(len(stones)):
            if stones[i] == minValue:
                local_zeros.append(i)
                stones[i] = 200000001

        zeros.extend(local_zeros)

        zeros.sort()
        continuous_zero = 0
        local_continuous_zero = []
        for i in range(len(zeros)-1):
            if zeros[i+1] - zeros[i] == 1:
                continuous_zero += 1
            else:
                local_continuous_zero.append(continuous_zero)
                continuous_zero = 0

        local_continuous_zero.append(continuous_zero)
        print(answer, zeros, local_continuous_zero)

        if local_continuous_zero and max(local_continuous_zero) > k:
            return answer

        answer += minValue - base
        base = minValue

    return answer+1

print(f'result: {solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)}')
# print(f'result: {solution([1, 5], 1)}')
