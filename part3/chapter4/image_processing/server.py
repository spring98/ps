from flask import Flask, request, send_file
import uuid
import random
import cv2
import os
import time

number_directory = 'numbers/'
if not os.path.exists(number_directory):
    os.makedirs(number_directory)

image_directory = 'images/'
if not os.path.exists(image_directory):
    os.makedirs(image_directory)


def generate_image(path):
    # 1부터 N X N까지의 수를 담고, 순서를 랜덤으로 섞기
    n = random.randint(1, 8)
    arr = [i for i in range(1, n * n + 1)]
    random.shuffle(arr)

    # N X N 크기의 이미지 생성(N = 8이라면, 8 X 8 이미지 생성)
    rows = []
    for i in range(n): # 각 행(row)마다 N개의 수 이미지가 들어감
        row = []
        for j in range(n): # 각 열(column)
            img = cv2.imread(number_directory + str(arr[i * n + j]).zfill(2) + '.png')
            row.append(img)
        hori = cv2.hconcat(row)
        rows.append(hori)
    result = cv2.vconcat(rows)

    # 최종적으로 생성된 이미지를 저장
    cv2.imwrite(image_directory + path, result)

    # 랜덤으로 연산자 배열 생성 (각 원소는 '+' 혹은 '*' 중 하나)
    operators = ['+', '*']
    sampled = []
    # 각 행은 N개의 정수로 구성되므로, 연산자의 개수는 N - 1개
    for i in range(n - 1):
        sampled.append(random.choice(operators))

    # 특정 행(target row)에 대해 정답 계산하기
    target = random.randint(0, n - 1) # 랜덤한 행 설정
    data = arr[target * n:target * n + n]
    answer = data[0]
    for i in range(n - 1):
        if sampled[i] == '+':
            answer += data[i + 1]
        elif sampled[i] == '*':
            answer *= data[i + 1]

    # 최종적으로 N, 목표 행(target), 연산자 목록(operators), 정답(answer)를 반환
    return n, target, sampled, answer


app = Flask(__name__)
# 등록된 참가자마다 각 시도를 [auth_key: {stage, image, n, target, answer, start_time}, ...] 형태로 저장
candidates = {
    'ABCDEFGH12345678': {}
}
flag = 'IMAGE_PROCESS_KING'
time_limit = 500
total_stage = 100


@app.route('/start', methods=['GET'])
def start():
    access_token = request.headers.get('Access-Token')
    # 사전에 등록된 참가자가 아닌 경우
    if access_token not in candidates:
        return {
            'status': 'unknown candidate'
        }
    # 현재 시도에 대한 대한 키(auth_key) 발급
    auth_key = str(uuid.uuid4())
    stage = 1
    path = auth_key + "_" + str(stage) + '.png'
    n, target, sampled, answer = generate_image(path)
    data = {
        'stage': stage,
        'image': path,
        'n': n,
        'target': target,
        'answer': answer,
        'start_time': time.time()
    }
    candidates[access_token][auth_key] = data
    print(f'[New] {data}')
    # 클라이언트(client)에게 결과 반환
    return {
        'status': 'success',
        'auth_key': auth_key,
        'stage': stage,
        'image': path,
        'n': n,
        'target': target,
        'operators': ''.join(sampled)
    }


@app.route('/image', methods=['GET'])
def image():
    # 클라이언트(client)로부터 제출 받은 값
    filename = request.args.get('filename')
    if not os.path.isfile(image_directory + filename):
        return {
            'status': 'invalid file name'
        }
    return send_file(image_directory + filename, mimetype='image/png')


@app.route('/query', methods=['POST'])
def query():
    access_token = request.headers.get('Access-Token')
    # 사전에 등록된 참가자가 아닌 경우
    if access_token not in candidates:
        return {
            'status': 'unknown candidate'
        }
    params = request.get_json()
    # auth_key가 올바르지 않을 때
    auth_key = params['auth_key']
    if auth_key not in candidates[access_token]:
        return {
            'status': 'unknown authentication key'
        }
    # 제한 시간을 초과한 경우
    start_time = candidates[access_token][auth_key]['start_time']
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        return {
            'status': 'success',
            'result': 'time over'
        }
    # 클라이언트(client)로부터 제출 받은 값
    if 'value' not in params:
        return {
            'status': 'value is needed'
        }
    value = params['value']
    answer = candidates[access_token][auth_key]['answer']
    if answer == value:
        stage = candidates[access_token][auth_key]['stage'] + 1
        if stage == total_stage + 1: # 모든 스테이지를 클리어한 경우
            return {
                'status': 'success',
                'result': flag
            }
        path = auth_key + "_" + str(stage) + '.png'
        n, target, sampled, answer = generate_image(path)
        data = {
            'stage': stage,
            'image': path,
            'n': n,
            'target': target,
            'answer': answer,
            'start_time': start_time
        }
        candidates[access_token][auth_key] = data
        return {
            'status': 'success',
            'result': 'correct',
            'stage': stage,
            'image': path,
            'n': n,
            'target': target,
            'operators': ''.join(sampled)
        }
    else:
        return {
            'status': 'success',
            'result': 'wrong'
        }


app.run(host="localhost", port=5000)
