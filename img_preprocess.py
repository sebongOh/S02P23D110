import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing import image
from sklearn.utils import shuffle
# 여기서 이미지를 데이터화 하겠지?


def img_pre(img_path, captions):
    all_img_name = []
    all_caption = []

    # 각 캡션에 <start><end>토큰 추가
    for i in range(0, len(captions), 1):
        img_path = captions[i][0]

        for j in range(1, 6, 1):
            caption = ""
            caption += '<start>' + captions[i][j] + '<end>'

            all_img_name.append(img_path)
            all_caption.append(caption)

    # print(all_img_name)
    # print(all_caption)
    train_captions, img_name_vector = shuffle(
        all_caption, all_img_name, random_state=1)
    num_example = 3000
    train_captions = train_captions[:num_example]
    img_name_vector = img_name_vector[:num_example]

    return img_name_vector, train_captions


def preprocess_img(img_path, flag, target_size=250):
    # keras.preprocessing의 image클래스 호출

    # img_path : 이미지 파일 경로
    # target_size : 이미지 데이터 사이즈(리사이징 할때 필요)
    # load_img() : 이미지 파일 로딩
    # img_to_array() : 이미지 파일을 array로 변환

    img = image.load_img(img_path, target_size=(target_size, target_size))

    img_tensor = image.img_to_array(img)

    # 3차원 array에 이미지 샘플을 구분하기
    # np.expand_dims() : 1개 차원 추가
    # 3차원 -> 4차원
    img_tensor = np.expand_dims(img_tensor, axis=0)

    # flag가 True : 데이터 정규화 하기
    if flag == True:
        img_tensor /= 255.
        # print(img_tensor[0])

    # flag가 False : 데이터 정규화 X
    else:
        print(img_tensor[0])

        # 테스트 코드
        # plt.rcParams['figure.figsize'] = (10, 10)
        # plt.imshow(img_tensor[0])
        # plt.show()

        # 데이터 리턴
    return img_tensor
