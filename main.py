def solution(sequence):
    seq_length = len(sequence)

    def makePulse(data):
        pulse1 = []
        pulse2 = []

        for i in range(len(data)):
            if i % 2 == 0:
                pulse1.append(data[i])
                pulse2.append(-data[i])
            else:
                pulse1.append(-data[i])
                pulse2.append(data[i])

        return pulse1, pulse2

    prefix1, prefix2 = makePulse(sequence.copy())

    dp = [0] * seq_length
    dp[0] = prefix2[0]

    for i in range(1, seq_length):
        dp[i] = max(prefix2[i], prefix2[i] + dp[i - 1])
        print(dp, prefix2[i], prefix2[i] + dp[i - 1])

    print(dp)
print(f'result: {solution([2, 3, -6, 1, 3, -1, 2, 4])}')
