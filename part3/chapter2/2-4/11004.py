import sys
input = sys.stdin.readline

# n = 5
# k = 2
n, k = map(int, input().strip().split(' '))

input_data = list(map(int, (input().strip().split(' '))))
sorted_input_data = sorted(input_data)

print(sorted_input_data[k-1])
