from PIL import Image, ImageDraw, ImageFont
import os


number_directory = 'numbers/'
if not os.path.exists(number_directory):
    os.makedirs(number_directory)

# 텍스트 크기는 22로 설정
fnt = ImageFont.truetype("arial.ttf", 22)
# 단순히 1부터 64까지의 수에 대한 이미지를 생성
for number in range(1, 65):
    # RGB 모드로 40 X 40 크기의 이미지를 생성(배경 색상은 흰색)
    img = Image.new('RGB', (40, 40), color = (255, 255, 255))
    drawed = ImageDraw.Draw(img)

    # (8, 8)의 위치에 (0, 0, 0) = 검은색 색상으로 텍스트 그리기
    drawed.text((8, 8), str(number).zfill(2), font=fnt, fill=(0, 0, 0))

    # 이미지 저장하기
    img.save(f'{number_directory + str(number).zfill(2)}.png')
