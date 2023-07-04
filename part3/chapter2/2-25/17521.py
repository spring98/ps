
n, w = 10, 24
input_data = [5, 7, 5, 4, 2, 7, 8, 5, 3, 4]

coin_data = [5, 7, 5, 4, 2, 7, 8, 5, 3, 4]
for i in range(n-1, 0, -1):
    if input_data[i-1] < input_data[i]:
        coin_data[i-1] = coin_data[i]

print(input_data)
print(coin_data)

dif_data = []
for i in range(n):
    dif_data.append(coin_data[i] - input_data[i])

print(dif_data)

money = 0
for i, data in enumerate(dif_data):
    if data>0:
        pass

'''
    단순히 매 날짜를 기준으로 다음 날짜에 가격이 오른다면 사기 
    인접한 날짜의 차이만 계산하면 된다. 
'''






