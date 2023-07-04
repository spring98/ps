import itertools
import heapq
import sys
input = sys.stdin.readline

N, C = map(int, input().strip().split(' '))
arr = []
for _ in range(N):
    arr.append(int(input().strip()))

arr = sorted(arr, reverse=True)
max_heap = []

for nCr in itertools.combinations(arr, C):
    min_array = []
    for i in range(C-1):
        min_array.append(nCr[i] - nCr[i+1])
    heapq.heappush(max_heap, -min(min_array))

print(-heapq.heappop(max_heap))

'''
    time limit 걸림
    해설 : 이진탐색 사용(데이터 값의 범위가 작으면 계수정렬, 크면 이진탐색 사용해라)
        가장 인접한 공유기 사이의 최대 gap 을 이진탐색으로 찾는다.
    1. 집의 좌표 리스트를 정렬한다.
    2. (0, 1) 집좌표의 gap -> 최소 gap, (0, -1) 집좌표의 gap -> 최대 gap 잡는다.
    3. 최소 gap 과 최대 gap 의 //2 로 mid 값을 찾는다
    4. 공유기의 갯수가 불가능 하다고 판단되면 다시 반복하는데 이때 최대 gap 은 아까 mid 값 -1 로 해서 설정한다.
    5. 공유기의 갯수가 만족되었다면 이제 min gap 을 올려가면서 최대값을 구해가면 된다. 
    이진탐색은 재귀적, 반복문 으로 구현할 수 있는데 반복문으로 구현하는 것을 추천한다.
'''
