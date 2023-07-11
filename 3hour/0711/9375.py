# [실패]
from itertools import combinations
import sys

T = int(input())

for _ in range(T):
    wears = {
        # 'headgear': ['hat', 'turban', 'a'],
        # 'eyewear': ['sunglasses']
    }

    N = int(input())

    for _ in range(N):
        value, key = list(sys.stdin.readline().split())
        if key not in wears:
            wears[key] = [value]
        else:
            wears[key].append(value)

    answer = 0

    for i in range(1, len(wears)+1):
        for combination in combinations(wears.keys(), i):
            count = 1
            for key in combination:
                count *= len(wears[key])
                # print(wears[key])
            answer += count

    print(answer)
