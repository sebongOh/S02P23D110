from tensorflow.keras.layers import Embedding
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
import img_preprocess
import numpy as np
import matplotlib.pyplot as plt
from data import preprocess

import pickle

# 여기서 캡션(5개 코멘트)을 토큰화 된 캡션 쌍으로 만들겠지?


def tokenization(captions):
    samples = []
    # for i in range(len(captions)):
    samples.append("<start>" + captions[0][1] + "<end>")
    samples.append("<start>" + captions[0][2] + "<end>")
    samples.append("<start>" + captions[0][3] + "<end>")
    samples.append("<start>" + captions[0][4] + "<end>")
    samples.append("<start>" + captions[0][5] + "<end>")
    # samples = ['The cat sat on the mat.', 'The dog ate my homework.']
    # for i in range(len(samples)):
    #     samples[i] = "<start>" + samples[i] + "<end>"

    # 가장 빈도가 높은 1,000개의 단어만 선택하도록 Tokenizer 객체를 만듭니다.
    tokenizer = Tokenizer(num_words=10000)

    # 단어 인덱스를 구축합니다.
    tokenizer.fit_on_texts(samples[:100])

    # 문자열을 정수 인덱스의 리스트로 변환합니다.

    # # 직접 원-핫 이진 벡터 표현을 얻을 수 있습니다.
    # # 원-핫 인코딩 외에 다른 벡터화 방법들도 제공합니다!
    # one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')
    # print(one_hot_results)

    # 계산된 단어 인덱스를 구합니다.
    word_index = tokenizer.word_index
    word_cnt = tokenizer.word_counts
    word_docs = tokenizer.word_docs
    print('Found %s unique tokens.' % len(word_index))
    print(word_index)  # 많이 나온 순서
    print(word_cnt)  # 각 값이 나온 횟수
    print("a가 나온 횟수 : {}".format(word_cnt['a']))
    # print(word_docs)

    cap_leng = 30
    pad = 0
    start_num = word_index['start']  # start의 토큰값 가져오기
    end_num = word_index['end']  # end의 토큰값 가져오기

    # 원-핫 인코딩: 단어간 유사도를 파악하지 못하기 때문에, , , ,
    samples = tokenizer.texts_to_sequences(samples)
    for i in range(len(samples)):
        samples[i].extend([pad]*(cap_leng-len(samples[i])))

    # print(samples[:10])  # 변환된 토큰들pring, 값이 많아서 10개만 봄
# with open('tokens.txt', 'wb') as f:
#     pickle.dump(samples, f)  # pickle 방식으로 저장
    # word_cnt : 30이고, 단어 집합의 크기
    # 5 : 임베딩 벡터의 출력 차원.
    # input_length : 입력 시퀀스의 길이. 여기선 30
    Embedding(word_cnt, 5, input_length=cap_leng)
    model = Sequential()
    return samples
# with open('tokens.txt', 'rb') as f:
#     data = pickle.load(f)

# print(data[:10])  # 제대로 가져왔는지 윗값과 비교용
