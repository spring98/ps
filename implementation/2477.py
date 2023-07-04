K = int(input())
input_data = []

for _ in range(6):
    input_data.append(list(map(int, input().split())))

# print(input_data)

current_coord = []
current_x = 0
current_y = 0

for direction, value in input_data:
    # print(direction, value)
    if direction == 1:
        current_x += value
    elif direction == 2:
        current_x -= value
    elif direction == 3:
        current_y -= value
    else:
        current_y += value
    current_coord.append((current_x, current_y))

# print(current_coord)

abs_coord = []
for x, y in current_coord:
    abs_coord.append((abs(x), abs(y)))

# print(sorted(abs_coord, key=lambda coord: coord[0]))
# print(sorted(abs_coord, key=lambda coord: coord[1]))
# print(min(abs_coord))

x_sort = sorted(abs_coord, key=lambda coord: coord[0])
y_sort = sorted(abs_coord, key=lambda coord: coord[1])

x_min, x_max = x_sort[0][0], x_sort[-1][0]
y_min, y_max = y_sort[0][1], y_sort[-1][1]
x_half, y_half = x_sort[3][0], y_sort[3][1]

# print(x_min, x_max, y_min, y_max, x_half, y_half)

a, b = 0, 0
if (x_min, y_max) not in abs_coord:
    a = x_min
    b = y_max

if (x_max, y_min) not in abs_coord:
    a = x_max
    b = y_min

melon_square = x_max * y_max - (abs(x_half-a) * abs(y_half-b))

print(melon_square * K)


