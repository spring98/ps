import random
import cv2
import os

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

    # N X N 크기의 이미지 생성 (N = 8이라면, 8 X 8 이미지 생성)
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


print(generate_image('result.png'))
