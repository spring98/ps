import sys
input = sys.stdin.readline

N = int(input().strip())
cranes = list(map(int, input().strip().split(' ')))
M = int(input().strip())
boxs = list(map(int, input().strip().split(' ')))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

# print(cranes)
# print(boxs)
if max(cranes) < max(boxs):
    print(-1)
    exit()

count = 0
while boxs:
    for crane in cranes:
        for i in range(len(boxs)):
            if crane >= boxs[i]:
                boxs.pop(i)
                break
    count += 1

# # answer = []
# count = 0
# # box_count = 0
# while boxs:
#     for crane in cranes:
#         for i in range(len(boxs)):
#             # print(f'crane : {crane}, boxs[i] : {boxs[i]}')
#             if crane >= boxs[i]:
#                 # answer.append((crane, boxs[i]))
#                 boxs.pop(i)
#                 # box_count += 1
#                 break
#             # elif crane < boxs[i] and box_count == 0:
#             #     print(-1)
#             #     exit()
#     # box_count = 0
#     count += 1

print(count)
