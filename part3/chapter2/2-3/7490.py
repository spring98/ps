from itertools import product

answer = []

n = 3
integers = [str(i) for i in range(1, n+1)]
calc_data = list(product(['+', '-', ' '], repeat=n-1))

for calc in calc_data:
    string = ''
    for i in range(n-1):
        string += integers[i] + calc[i]
    string += integers[-1]
    if eval(string.replace(' ', '')) == 0:
        print(string)

'''
    원래 재귀적으로 푸는 것이 해설인데 product 로 풀 수 있을 것 같아서 해봄
    근데 되는 것 같음, 저지에는 안올려봄
'''