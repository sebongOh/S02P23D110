from data import preprocess
from sklearn.model_selection import train_test_split  # 데이터를 학습용/테스트용으로  분리해주는 유틸리티
import my_token
import img_preprocess
import img_extract
import create
import CNN
import RNN
# - 이미지 데이터 불러오기 링크
# https://m.blog.naver.com/PostView.nhn?blogId=baek2sm&logNo=221400912923&categoryNo=36&proxyReferer=https%3A%2F%2Fwww.google.com%2F

# - Augmentation 링크
# https://keraskorea.github.io/posts/2018-10-24-little_data_powerful_model/


# Req 3번에서 이미지 파일 경로랑 캡션을 입력으로 받으라고 함
#  이미지 파일 경로, 캡션 받기
img_paths, captions = preprocess.get_path_caption()
# ===========================
# 이미지 정규화 데이터 받아오기
# 여기 구현
img_name_vector, train_captions = img_preprocess.img_pre(img_paths, captions)
# ===========================


# ===========================================
# 캡션 토큰화 데이터 받아오기,, 리턴은 토크나이저
# my_tokenizer = None
# if(token.Load_Tokenizer is None):
my_tokenizer, cap_vector = my_token.tokenization(train_captions[:10000])
# ===========================================


# ==================
# 토크나이저 저장하기
my_token.Save_Tokenizer(my_tokenizer)
# 토크나이저 불러오기
my_tokenizer = my_token.Load_Tokenizer()
# ==================


# =============================
# 학습/테스트용 데이터로 분할하기
# (학습용 80% / 테스트용 20%로 설정)
# test_size가 0.2이면 train_size는 0.8
# 따라서 train:test = 80% : 20%
img_name_train, img_name_test, cap_train, cap_test = train_test_split(
    img_name_vector, cap_vector, test_size=0.2, random_state=0)
# ====================-=======

# tf 데이터셋 만들기
dataset = create.create_tf_data(my_tokenizer, img_name_train, cap_train)


# 환경 변수
embedding_dim = 256
units = 512
vocab_size = my_token.top_k + 1

# 모델 학습
encoder = CNN.CNN_Encoder(embedding_dim)
decoder = RNN.RNN_Decoder(embedding_dim, units, vocab_size)
