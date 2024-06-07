from collections import defaultdict

BO = 'bo'
GIDOONG = 'gidoong'
def solution(n, build_frame):
    answer = []
    build_map = defaultdict(list)
    build_map2 = defaultdict(list)

    # a
    for x, y, a, b in build_frame:
        # 기둥
        if a == 0:
            # 설치
            if b == 1:
                # 설치 가능
                if y == 0 or (x, y) in build_map[BO] or (x, y) in build_map[GIDOONG]:
                    build_map[GIDOONG].append((x, y))
                    build_map[GIDOONG].append((x, y+1))
                    build_map2[GIDOONG].append((x, y))

            # 삭제
            else:
                # 삭제할 기둥 위에 기둥인 경우
                if (x, y+1) in build_map[GIDOONG]:
                    if (x, y+1) in build_map[BO]:
                        build_map[GIDOONG].remove((x, y))
                        build_map[GIDOONG].remove((x, y+1))
                        build_map2[GIDOONG].remove((x, y))

                # 삭제할 기둥 위에 보인 경우
                if (x, y + 1) in build_map[BO]:
                    if (x-1, y+1) in build_map[BO]:
                        build_map[GIDOONG].remove((x, y))
                        build_map[GIDOONG].remove((x, y + 1))
                        build_map2[GIDOONG].remove((x, y))
        # 보
        else:
            # 설치
            if b == 1:
                if (x, y) in build_map[GIDOONG] or (x+1, y) in build_map[GIDOONG] or ((x, y) in build_map[BO] and (x+1, y) in build_map[BO]):
                    build_map[BO].append((x, y))
                    build_map[BO].append((x+1, y))
                    build_map2[BO].append((x, y))

            # 삭제
            else:
                pass

    for x, y in build_map2[GIDOONG]:
        answer.append((x, y, 0))

    for x, y in build_map2[BO]:
        answer.append((x, y, 1))

    answer = list(set(answer))
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    answer2 = []

    for a, b, c in answer:
        answer2.append([a, b, c])

    return answer2


print(f'result: {solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])}')
