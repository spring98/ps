import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dictionary = {}
for _ in range(N):
    team = input().strip()
    members = int(input())
    for _ in range(members):
        if team not in dictionary.keys():
            dictionary[team] = [input().strip()]
        else:
            dictionary[team].append(input().strip())

for _ in range(M):
    query = input().strip()
    query_num = int(input())

    # team의 멤버들 호출
    if query_num == 0:
        for data in sorted(dictionary[query]):
            print(data)

    # 멤버가 속한 team 호출
    else:
        for key, value in dictionary.items():
            if query in dictionary[key]:
                print(key)
