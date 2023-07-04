
# y_count, x_count = 3, 5
#
# rectangle = [
#     [4, 2, 1, 0, 1],
#     [2, 2, 1, 0, 0],
#     [2, 2, 1, 0, 1],
# ]

y_count, x_count = list(map(int, input().split()))

rectangle = []
for _ in range(y_count):
    sequence = ' '.join(input())
    rectangle.append(list(map(int, sequence.split())))

# print(rectangle)

adder = 1
square_level = 1
x, y = 0, 0
while True:
    if x + adder < y_count:
        # print(rectangle[x][y], rectangle[x][y+adder])
        # print(rectangle[x+adder][y], rectangle[x+adder][y+adder])
        if rectangle[x][y] == rectangle[x][y+adder] == rectangle[x+adder][y] == rectangle[x+adder][y+adder]:
            square_level = adder+1
        # print()
        x += 1
    else:
        x = 0
        y += 1
        if y + adder < x_count:
           pass
        else:
            x = 0
            y = 0
            adder += 1

    if adder+1 >= y_count and adder+1 >= x_count:
        break

print(square_level * square_level)
