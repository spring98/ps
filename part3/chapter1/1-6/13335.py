import sys

input = sys.stdin.readline

N, W, L = [4, 2, 10]
trucks = [7, 4, 5, 6]
bridge = [0]*W
count = 0

while True:
    bridge.pop()

    if sum(bridge) + trucks[0] >= L:
        truck = trucks.pop(0)
        bridge.append(truck)
    else:
        bridge.append(0)


'''
    아이디어는 맞는데 구현을 못했다.
'''