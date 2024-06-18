def solution(alp, cop, problems):
    alps = []
    cops = []
    alp_max = 0
    cops_max = 0

    for a, b, c, d, e in problems:
        alps.append(a)
        cops.append(b)

    alp_max = max(alps)
    cops_max = max(cops)
    alp = min(alp, alp_max)
    cop = min(cop, cops_max)

    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])

    dp = [[float('inf') for _ in range(cops_max+1)] for _ in range(alp_max+1)]
    dp[alp][cop] = 0

    for a in range(alp, alp_max+1):
        for c in range(cop, cops_max+1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= a and cop_req <= c:
                    new_alp = min(a + alp_rwd, alp_max)
                    new_cop = min(c + cop_rwd, cops_max)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[a][c] + cost)

    # for d in dp:
    #     print(d)

    return dp[alp_max][cops_max]

print(f'result: {solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]])}')
print(f'result: {solution(0,0,[[0,5,2,1,2],[10,10,3,3,4]])}')
print(f'result: {solution(0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])}')
