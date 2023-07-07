# [성공]
# N = 4
# distances = [2, 3, 1]
# cities = [5, 2, 4, 1]

N = int(input())
distances = list(map(int, input().split()))
cities = list(map(int, input().split()))

min_city = 1000000001
answer = 0

while len(cities) > 1:
    city = cities.pop(0)
    min_city = min(min_city, city)
    distance = distances.pop(0)
    answer += (min_city * distance)

print(answer)
