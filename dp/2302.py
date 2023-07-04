# 극장 좌석 [성공]

fibo = [0 for _ in range(42)]
fibo[0] = 0
fibo[1] = 1
fibo[2] = 2

for i in range(3, 42):
    fibo[i] = fibo[i-2] + fibo[i-1]

# print(fibo)

N = int(input())
N_list = [i for i in range(1, N+1)]
N_list.append(-1)

M = int(input())

for _ in range(M):
    N_list[int(input())-1] = -1

# print(N_list)

count = 0
count_list = []

for N in N_list:
    if N != -1:
        count += 1
    else:
        count_list.append(count)
        count = 0

# count_list.append(count)
# count = 0

# print(count_list)

answer = 1
for count in count_list:
    if count != 0:
        answer *= fibo[count]

print(answer)

# count_list 에 0이 들어 가는 경우는 fibo 가 0이 되니까 answer=0 이 되므로 예외 처리
