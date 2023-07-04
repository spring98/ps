import sys
input = sys.stdin.readline

N = int(input().strip())
info_dict = dict()

for _ in range(N):
    dead_line, cup = map(int, input().strip().split(' '))
    if dead_line not in info_dict:
        info_dict[dead_line] = [cup]
    else:
        info_dict[dead_line].append(cup)

answer = 0
keys = list(info_dict.keys())
keys.sort()
# print('--------------')
for time in range(1, N+1):
    for dead_line in keys:
        if time <= dead_line:
            # print(time, dead_line)
            if info_dict[dead_line]:
                # print(info_dict[dead_line].pop(info_dict[dead_line].index(max(info_dict[dead_line]))))
                answer += info_dict[dead_line].pop(info_dict[dead_line].index(max(info_dict[dead_line])))
            break

print(answer)


# for time in range(1, N+1):
#
#             # answer += max(item[1])
#
# print(answer)

'''
    해설
    데드라인을 기준으로 오름차순 정렬을 수행한다.
    각 문제의 컵라면 수를 우선순위 큐에 넣으면서, 
    데드라인을 초과하는 경우에는 최소 원소를 제거한다.
    우선순위큐의 원소의 개수가 데드라인과 같게 볼 수 있다.
'''
