n = int(input())
input_data = list(map(int, input().split()))

input_data.sort(reverse=True)

for i in range(n):
    input_data[i] += 2+i

print(max(input_data))
