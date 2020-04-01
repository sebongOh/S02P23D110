from data import preprocess
import create

# - 이미지 데이터 불러오기 링크
# https://m.blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221400912923&categoryNo=36&proxyReferer=https%3A%2F%2Fwww.google.com%2F

# - Augmentation 링크
# https://keraskorea.github.io/posts/2018-10-24-little_data_powerful_model/


# Req 3번에서 이미지 파일 경로랑 캡션을 입력으로 받으라고 함
#  이미지 파일 경로, 캡션 받기
img_paths, captions = preprocess.get_path_caption()


# 캡션 1개의 행에 5개의 comment가 있음
# for i in range(len(captions)):
#     # 한개의 이미지 경로, 한개의 이미지에 해당하는 캡션
#     create.create_dataSet(img_paths, captions[i])


create.create_dataSet(img_paths, captions[0])
