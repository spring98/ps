import json
import requests
from PIL import Image
from numpy import asarray

BASE_URL = 'http://127.0.0.1:5000/'
headers = {
    'Access-Token': 'ABCDEFGH12345678',
    'Content-Type': 'application/json'
}

auth_key = ''
image = ''
n = -1
operators = ''
target = -1


def start_api():
    global auth_key, image, n, operators, target
    response = requests.get(BASE_URL + 'start', headers=headers)
    json_data = json.loads(response.text)

    auth_key = json_data['auth_key']
    image = json_data['image']
    n = json_data['n']
    operators = json_data['operators']
    target = json_data['target']


def image_api():
    response = requests.get(BASE_URL + f'image?filename={image}')
    # image_data = response.content

    save_path = 'ps_image.png'
    photo = open(save_path, 'wb')
    photo.write(response.content)
    photo.close()

    # load the image
    image_png = Image.open(save_path)
    # convert image to numpy array
    data = asarray(image_png)
    print(type(data))
    # summarize shape
    print(data.shape)

    # create Pillow image
    image2 = Image.fromarray(data)
    print(type(image2))

    # summarize image details
    print(image2.mode)
    print(image2.size)

    print(data)

    # print(len(image_data))
    # print(n*n*40*40)
    # image_arr = np.frombuffer(image_data, dtype=np.float64)
    # print(image_arr)
    # print(image_arr[1])




start_api()
image_api()
