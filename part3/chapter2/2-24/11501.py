import heapq

input_data = [1, 1, 3, 1, 2]
max_heap = []
dp = [0] * 10001

for i, data in enumerate(input_data):
    heapq.heappush(max_heap, (-data, i))

criterion_value = -1
criterion_index = 0

while max_heap:
    value, index = heapq.heappop(max_heap)
    print(-value, index)
    if criterion_value > -value:
        pass


'''
    각 날짜별로 뒤에오는 날짜의 주가중에서 최대 값을 알아내면 된다.
      7  8 10  9 12 7 4 5
  -> 12 12 12 12 12 7 5 5
    뒤에서 부터 하나씩 보면서 더 큰 값을 만날 때 까지 최댓값을 기록한다. ㅋㅋ
'''


