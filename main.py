def solution(commands):
    answer = []
    N = 50
    table = [['' for _ in range(N+1)] for _ in range(N+1)]
    merge_map = []

    def update(comm):
        # 모든 value1 를 value2 로 변경
        if len(comm) == 3:
            value1, value2 = comm[1], comm[2]
            for r in range(N + 1):
                for c in range(N + 1):
                    if table[r][c] == value1:
                        table[r][c] = value2

        # (r, c) 의 값을 value 로 변경
        elif len(comm) == 4:
            r, c, value = int(comm[1]), int(comm[2]), comm[3]
            myIndex = -1
            for i, m in enumerate(merge_map):
                if (r, c) in m:
                    myIndex = i
                    break

            if myIndex == -1:
                table[r][c] = value
            else:
                for _r, _c in merge_map[myIndex]:
                    table[_r][_c] = value

    def merge(r1, c1, r2, c2):
        if (r1, c1) == (r2, c2):
            return

        index1 = -1
        index2 = -1
        for i, m in enumerate(merge_map):
            if (r1, c1) in m:
                index1 = i

            if (r2, c2) in m:
                index2 = i

        if index1 != -1 and index2 != -1:
            merge_map[index1] = merge_map[index1].union(merge_map[index2])
            merge_map.pop(index2)

        if index1 != -1 and index2 == -1:
            merge_map[index1].add((r2, c2))

        if index1 == -1 and index2 != -1:
            merge_map[index2].add((r1, c1))

        if index1 == -1 and index2 == -1:
            merge_map.append({(r1, c1), (r2, c2)})

        # print(merge_map, len(merge_map), index1, index2, r1, c1, r2, c2)
        myIndex = -1
        myValue = ''
        for i, m in enumerate(merge_map):
            if (r1, c1) in m:
                myIndex = i
                break

        if myIndex != -1:
            if table[r1][c1]:
                for r, c in merge_map[myIndex]:
                    table[r][c] = table[r1][c1]
            else:
                for r, c in merge_map[myIndex]:
                    if table[r][c]:
                        myValue = table[r][c]
                        break

                for r, c in merge_map[myIndex]:
                    table[r][c] = myValue

    def unmerge(param_r, param_c):
        myIndex = -1
        myValue = table[param_r][param_c]
        for i, m in enumerate(merge_map):
            if (param_r, param_c) in m:
                myIndex = i
                break

        if myIndex != -1:
            for r, c in merge_map[myIndex]:
                table[r][c] = ''

        table[param_r][param_c] = myValue

    def table_print(r, c):
        if table[r][c]:
            answer.append(table[r][c])
        else:
            answer.append('EMPTY')

    def pppp():
        for t in table:
            print(t)
        print()

    for command in commands:
        comm = list(command.split(' '))
        if comm[0] == 'UPDATE':
            update(comm)

        elif comm[0] == 'MERGE':
            merge(int(comm[1]), int(comm[2]), int(comm[3]), int(comm[4]))

        elif comm[0] == 'UNMERGE':
            unmerge(int(comm[1]), int(comm[2]))

        # (r, c) 의 값을 출력
        elif comm[0] == 'PRINT':
            table_print(int(comm[1]), int(comm[2]))

    # pppp()
    return answer

print(f'result: {solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])}')
# print(f'result: {solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])}')
