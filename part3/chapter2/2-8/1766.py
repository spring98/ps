import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split(' '))

problems = [i+1 for i in range(N)]
# print(problems)

sequence = {}
input_data = []
for _ in range(M):
    input_data.append(list(map(int, input().strip().split(' '))))

for data in input_data:
    first, second = data
    sequence[second] = first
    problems.pop(problems.index(first))

# print(sequence)

for problem in problems:
    if problem in sequence:
        print(sequence[problem], end=' ')
    print(problem, end=' ')

'''
    해설
    전형적인 위상정렬 문제
    순서가 정해져있는 작업을 차례대로 수행해야 할 때 순서를 결정해주는 알고리즘이다.
    위상정렬 알고리즘
    1. 진입차수가 0인 정점을 큐에 삽입한다.
    2. 큐에서 원소를 꺼내 원소와 간선을 제거한다.
    3. 제거 이후에 진입차수가 0이 된 정점을큐에 삽입한다.
    4. 큐가빌때 까지 2,3 과정을 반복한다.
    
    모든 원소를 방문하기전에 큐가 빈다면 사이클이 존재하는 것
    모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상정렬의 결과이다.
'''