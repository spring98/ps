N, K = 4, 7
input_data = [
    [6, 13],
    [4, 8],
    [3, 6],
    [5, 12],
]

bag_list = []
for data in input_data:
    W, V = data
    ratio = V/W
    bag_list.append((ratio, W, V))

print(sorted(bag_list, reverse=True))

'''
    해설
    knapsack problem O(NK) 에 2차원 배열로 풀 수 있다.
    모든 무게에 대하여 최대가치를 저장한다.
    D[i][j] = 배낭에 넣은 물품의 무게 합이 j 일때 얻을 수 있는 최대 가치
    각 물품번호 i 에 따라서 최대 가치 테이 D[i][j]를 갱신하여 문제를 해결할 수 있다.
    
    D[i][j] -> j < W[i] : D[i-1][j]
            -> j >= W[i] : max(D[i-1][j], D[i-1][j-W[i]]+V[i])
    
'''

