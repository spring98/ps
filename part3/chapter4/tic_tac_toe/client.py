import requests
import json
from itertools import combinations

BASE_URL = 'http://127.0.0.1:5000/'
headers = {
    'Access-Token': 'ABCDEFGH12345678',
    'Content-Type': 'application/json'
}
auth_key = ''
position = ''


def start_api():
    global auth_key
    global position
    response = requests.get(BASE_URL + 'start', headers=headers)
    auth_key = json.loads(response.text)['auth_key']
    position = json.loads(response.text)['position']


def query_api(pos):
    body = {
        'auth_key': auth_key,
        'position': pos
    }
    response = requests.post(BASE_URL + 'query', data=json.dumps(body), headers=headers)
    print(response.text)


coord_to_num = {
    '(0,0)': 2, '(1,0)': 7, '(2,0)': 6,
    '(0,1)': 9, '(1,1)': 5, '(2,1)': 1,
    '(0,2)': 4, '(1,2)': 3, '(2,2)': 8,
}

num_to_coord = {
    2: '(0,0)', 7: '(1,0)', 6: '(2,0)',
    9: '(0,1)', 5: '(1,1)', 1: '(2,1)',
    4: '(0,2)', 3: '(1,2)', 8: '(2,2)',
}

computer = []
user = []

start_api()
# while True:
#     print(position)
#     if position == 'none':
#         query_api(num_to_coord[5])
#         user.append(5)
#
#     elif position == '(1,1)':
#         query_api(num_to_coord[1])
#         user.append(1)
#
#     else:
#         for item in combinations(computer, 2):
#             first, second = item
#             key = 15 - first - second
#             if key not in user:
#                 if 0 < key < 10:
#                     query_api(num_to_coord[key])
#                     user.append(key)
#
#
#     computer.append(coord_to_num[position])


'''
    해설
    minimax 알고리즘 
    두 사람이 번갈아 싸우는 zero sum 게임에서 사용할 수 있는 알고리즘 
    효용함수를 정의하고 두명의 플레이어는 각자 목적에 맞게 행동한다.
    max 플레이어는 효용을 최대화, min 플레이어는 효용을 최소화 한다.
    재귀 함수(깊이 우선탐색)을 이용해 구현할 수 있다.
'''
