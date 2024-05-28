# [실패]

N = int(input())
ropes = []

for _ in range(N):
    ropes.append(int(input()))

print(min(ropes) * N)
