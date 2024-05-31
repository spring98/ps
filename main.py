def solution(tickets):
    answer = []
    graph = {}

    for start, end in tickets:
        if start not in graph:
            graph[start] = [end]

        else:
            graph[start].append(end)
            graph[start].sort(reverse=True)

    def dfs():
        need_visit = ['ICN']

        while need_visit:
            node = need_visit.pop()
            answer.append(node)

            # if node in graph and graph[node]:
            #     need_visit.append(graph[node].pop(0))

            if node in graph and graph[node]:
                need_visit.extend(graph[node])
                graph[node] = []

                # print(graph, '     ', need_visit, '     ', node)

    dfs()

    return answer

print(f'result: {solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])}')
# print(f'result: {solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])}')
# print(f'result: {solution([["ICN", "B"], ["B", "C"], ["C", "INC"]])}')
