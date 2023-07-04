from collections import deque

N = int(input())
input_data = list(map(int, input().split()))
balloons = deque()

for i, data in enumerate(input_data):
    balloons.append((data, i+1))

while balloons:
    rotations, balloon = balloons.popleft()
    print(balloon, end=' ')
    if rotations > 0:
        balloons.rotate(-rotations+1)
    else:
        balloons.rotate(-rotations)


