import tokenization
import img_preprocess
import Augmentation


def create_dataSet(img_paths, captions):

    # 이미지 데이터화해서 받아오기
    # img_tensor = img_preprocess.preprocess_img(captions[0], True)

    # 토큰화 된 캡션 쌍 받아오기
    caption_sample = tokenization.tokenization(captions)

    # tf 데이터형식 지키는건진 모르겠움,,
    # 이미지는 tf파일 형식으로 바꿔서 리턴한거라서 ㄱㅊ
    # 토큰화된 캡션에서는 잘 모르겠음?
    # return img_tensor, caption_sample
    # Augmentation.do(img_tensor)
