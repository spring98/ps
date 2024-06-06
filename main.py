def solution(scores):
    score_list = []
    wanho = scores[0]

    for a, b in scores:
        score_list.append((a+b, a, b))

    score_list.sort(reverse=True)

    # print(score_list)
    end_index = 0
    for i, score in enumerate(score_list):
        if score[0] <= wanho[0]+wanho[1]:
            end_index = i
            break

    highest_list = score_list[:end_index].copy()
    answer = len(highest_list)

    for i in range(len(highest_list)-1):
        for j in range(i+1, len(highest_list)):
            s1, a1, b1 = highest_list[i]
            s2, a2, b2 = highest_list[j]

            if a1 < a2 and b1 < b2:
                if a1 == wanho[0] and b1 == wanho[1]:
                    return -1

                answer -= 1

            if a2 < a1 and b2 < b1:
                if a2 == wanho[0] and b2 == wanho[1]:
                    return -1

                answer -= 1

    return answer+1

print(f'result: {solution([[2,2],[1,4],[3,2],[3,2],[2,1]]	)}')
