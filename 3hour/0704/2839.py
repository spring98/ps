
N = int(input())
# N = 4

M = N

count = M // 5
M = M % 5

if M == 0:
    print(count)
else:
    while M % 3 != 0:
        count -= 1
        M += 5
        if N < M:
            print(-1)
            quit()
    count += M // 3
    print(count)
