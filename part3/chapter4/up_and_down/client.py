import requests
import json

BASE_URL = 'http://127.0.0.1:5000/'
ACCESS_TOKEN = 'spring-access-token'
headers = {
    'Content-Type': 'application/json',
    'Access-Token': ACCESS_TOKEN
}


def start_apt():
    response = requests.post(BASE_URL + 'start', headers=headers)
    print(response.text)
    return response.text


def query_api(value):
    string_auth_key = start_apt()
    auth_key = json.loads(string_auth_key)['auth_key']

    body = {
        'auth_key': auth_key,
        'value': value
    }

    response = requests.post(BASE_URL + 'query', headers=headers, data=json.dumps(body))
    print(response.text)
    return response.text


while True:
    results = query_api(int(input()))
    server_value = json.loads(results)['result']
    if server_value == 'up':
        print('더 큰 값을 입력하세요.')
    elif server_value == 'down':
        print('더 작은 값을 입력하세요.')
    else:
        print('정답!!!')
        break

