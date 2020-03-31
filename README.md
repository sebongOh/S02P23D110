# 🐥 인공지능 프로젝트

<br>

## Core Team 😜

<table>
   <tr>
      <td>
        <img width="160px" src="https://lab.ssafy.com/webmobile1-sub1/s02p11d138/raw/develop/KakaoTalk_20200109_090135135.jpg"><br>
         [홍성욱](https://github.com/Woogie924)<br>
         <i>Project lead & Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
   </tr>
</table>

## 🤲 OverView<br>

### Goal

> - 인공지능과 머신 러닝에 대한 이해
> - 선형 회귀 및 경사 하강법에 대한 이해
> - 선형 회귀 모델 구현
> - 이미지 캡셔닝 데이터 전처리
> - 데이터 시각화

### 📌주요 라이브러리 및 프레임워크

- **Numpy**
  - Scientific Computing을 파이썬에서 가능하게 하기 위해 만들어진 Python 패키지
- **Matplotlib**
  - 데이터 시각화를 위해 사용되는 파이썬 라이브러리
- **Tensorflow**
  - 구글에서 제공하는 머신러닝을 위한 **End-to-End**오픈소스 플랫폼
  - **Tensorboard** 시각화 툴을 제공-> 학습 과정 및 연산 그래프, 결과를 확인하기 쉬움
- **Keras**
  - Python으로 작성되었으며, Tensorflow,CNTK,Teeano와 같은 Deep Learning 라이브러리 위에서 실행할 수 있는 High-level Neural Network API
  - 모듈성과 쉬운 확장성
- **json**
- **argsparse**

## 🎫 기능/과제 목록

### 진척률 100%

<table>
<tr><th>Req</th><th>Category</th></tr>
<tr><td>1</td><td>단순 선형 회귀 모델 구현</td></tr>
<tr><td>2</td><td>이미지 캡셔닝 Configuration</td></tr>
<tr><td>3</td><td>이미지 캡셔닝 데이터 전처리</td></tr>
<tr><td>4</td><td>데이터 시각화</td></tr>
</table>
<br>

## 🎲 파일/디렉터리 구조

- checkpoints/
  > 학습된 모델들이 저장되는 폴더
- data/
  > 데이터 처리 함수들이 위치한 폴더
- datasets/
  > 실제 데이터가 위치한 경로
- models/
  > 이미지 캡셔닝 모델이 위치한 경로
- utils/
  > 데이터 시각화, 학습 및 테스트에 필요한 유틸리티 함수들이 위치한 경로
- config.py
  > 설정 변수들이 저장된 파일
- linear_regression.py
  > 선형 회귀 모델의 학습 및 시각화 예시코드가 있는 파일
- predict.py
  > 학습된 모델을 사용해 새로운 데이터에 대해 결과값을 예측하는 파일
- train.py
  > 캡셔닝 모델 학습 파일

## 🤦 SetUp

### 아나콘다 설치

- [아나콘다 다운로드 링크](https//www.anaconda.com/distribution/) 접속후 version 3.7 다운로드

- 아나콘다 가상 환경 생성 및 활성화

  ```bash
  conda create -n AI python = 3.7
  conda activate AI
  ```

- Tensorflow 및 필요 라이브러리 설치

  ```bash
  conda install git matplotlib scikit-learn tqdm scipy numpy tesorflow-gpu=2.0.0
  ```

- 샘플 실행 확인
  ```bash
  <!--프로젝트 최상단 디렉토리에서 할 것.-->
  python linear_regression.py
  ```

### 이미지 다운로드

- 이미지 데이터 다운로드: [https://i02lab1.p.ssafy.io/images.zip (4.07GB)](https://i02lab1.p.ssafy.io/images.zip)
- 다운로드 받은 파일을 datasets 폴더에서 압축 해제

### VSCode로 아나콘다 사용하기

- 참고 링크 : [참고링크](https://blog.naver.com/PostView.nhn?blogId=sbd38&logNo=221353609570&parentCategoryNo=&categoryNo=31&viewDate=&isShowPopularPosts=true&from=search)

## 🎈 Knowledge

### 머신러닝, 딥러닝

> 인공지능은 인간의 지능에 가까운 기능을 갖춘 컴퓨터 시스템
> **머신러닝은 이러한 인공지능 시스템을 구현하는 구체적인 접근 방식**

- 컴퓨터가 데이터를 학습함으로써, 기존 데이터와 유사하지만 처음보는 데이터를 자동으로 해석할 수 있게 하는 기법
- 명시적 프로그래밍이라고도 한다. > 컴퓨터에게 어떻게 동작할지, 사람이 코드를 통해 명시적으로 지시함.

#### 최적화 알고리즘 찾기

1. 관계가 선형 관계인지, 비선형 형태인지?
2. 모델 선택(예를 들어 1차 선형관계를 선택했다고 하자)
3. 최적의 변수를 찾아야한다.
4. 최적이 존재하려면 다른 변수와 비교할 수 있는 척도가 필요하다

   > 이때 바로 손실 함수(Cost Function)가 필요하다.

### 딥 러닝이란?

> 심층 신경망(Deep Neural network)을 사용한 머신 러닝

#### Deep Neural Network

> 더 복잡하고 다양한 특성 정보를 얻기 위해서 2개 이상의 신경망층을 쌓은 모델

#### 인경 신경망

> 머신 러닝 방법 중 생물학적 신경망의 시냅스 결함을 모방한 모델

### 선형 회귀(Linear Regression)

- 주어진 데이터를 가장 잘 설명하는 직선을 찾는 문제

  - Y = WX + B 형태 ( W = 기울기 , B = 편차)

- [경사하강법](https://www.youtube.com/watch?v=ve6gtpZV83E)

### 손실함수

- 모델을 선택한 후에는 최적의 변수를 찾아야하는데, 최적이 존재하려면 서로 다른 변수의 조합들을 비교할 수 있는 척도가 필요함 ==> 이때 사용 되는 것이 손실함수

- 하나만 있는 게 아니라 프로젝트의 목표에 따라 다르게 정의되고 변형

- 대표적으로 사용되는 함수

  - 평균 제곱 편차 (i=1 ~~ i=N)
    $$
    MSE = 1/n∑(y_i-y_i^*)^2
    $$

- 최적화 방법 == [경사하강법](https://www.youtube.com/watch?v=ve6gtpZV83E)

## 💎 구현

### 🔎단순 선형 회귀 모델 구현

#### 데이터 읽기 및 시각화

##### 데이터 읽어오기

- np.load : 해당 경로의 npy파일을 읽어오기

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

train_data = np.load(".\\datasets\\linear_train.npy")
print(train_data)
```

##### 데이터 다듬기

- expend_dims
  - 차원을 늘리는 함수
  - x값들을 각각 리스트에 넣기 위해 axis를 1로 사용
  - 0이면 `x_data = train_data[:,0]`과 동일

```python
x_data = np.expand_dims(train_data[:,0], axis=1)
y_data = train_data[:,1]
```

##### 데이터 표시

- plt.scatter
  > scatter(y,x,s,c)
  - `x`: x축 값을 배열로 입력
  - `y`: y축 값을 배열로 입력
  - `s`: 점의 크기
  - `c`: 점의 색상
- plt.legend
  > legend()
  - 범주를 자동으로 잡아준다.
  - 괄호안에 `predict data`를 입력하면 라벨에 `predict data`가 입력
- plt.show
  - 그래프 그리기

#### 선형 모델 클래스 생성

linear_model.py에 생성되어 있는 LinearModel클래스 불러오기

```python
from models.linear_model import LinearModel

model = LinearModel(1)
```

##### call 호출 테스트

```python
print(model.call(tf.fill([1, 1], 10)))
```

#### 최적화 함수 및 손실 함수 바인딩

- `tf.keras.optimizers`
  - 학습 과정 설정
  - Adadelta, Adagrad, Adam , Adamax, Frtl, Nadam, Optimizer, RMSprop, SGD 등이 있음
  - 일차함수를 계산하기 위하여 SGD를 사용
  ```python
  tf.keras.optimizers.SGD(learning_rate, momentum, nesterov, name)
  ```
        - learning_rate : 학습속도
        - momentum : 해당 방향으로 SGD를 가속화하고 진동을 완화(0~1)
        - nesterov : nesterov 운동량 적용 여부
        - name : 이름
        - loss : 최적화 과정에서 최소화될 손실함수 설정
            - MSE : mean_squared_error
        - metrics
            - MeanSquaredError() : `y_true`와 `y_pred`사이의 평균 제곱 로그 오류 계산
  - metrics : 훈련을 모니터링하기 위해 사용

#### 모델 학습 함수 구현

```python
model.fit(x=x_data,
		  y=y_data,
		  epochs=10,
		  batch_size=32)
```

- `x` : 입력 데이터
- `y` : 라벨 값
- `batch_size` : 몇 개의 샘플로 가중치를 갱신할 것인지 지정
  - 얼마나 진행한 뒤 비교하는지 지정. 클수록 가중치 갱신이 적어짐
- `epochs` : 같은 자료로 반복학습할 횟수

#### 예측 결과 시각화

> predict로 기존값들을 선으로 나타내고, linear_test_x를 예측값으로 만듬

```python
test_x = np.load(".\\datasets\\linear_test_x.npy")


calculate_degree = model.predict(x=x_data,
    					   		 batch_size=2)

prediction = model.predict(x=test_x,
    					   batch_size=2)

plt.scatter(x_data,y_data,s=20,label="linear train")
plt.scatter(x_data,calculate_degree,s=5,c="b",label="prediction data")
plt.scatter(test_x,prediction,s=5,c="r",label="prediction data")
plt.legend(['savedata', 'learndata', 'predict'])
plt.show()
```

### 🔎이미지 캡셔닝 Configuration

- config.py

```python
import argparse

# Req. 2-1	Config.py 파일 생성

# 인자값을 받을 수 있는 인스턴스 생성
parser = argparse.ArgumentParser(description='이미지 캡셔닝 모델 Setting..')

# 입력받을 인자값 등록
# 캡션 데이터가 저장된 csv 파일의 경로
parser.add_argument('--caption_file_path', type=str,
                    default='.\\datasets\\captions.csv')
# 실제 이미지 파일들이 저장된 경로
parser.add_argument('--image_file_path', type=str,
                    default='.\\datasets\\images\\')

# 샘플링 추출할 갯수
parser.add_argument('-s', '--do_sampling', type=int,
                    help="샘플링 여부 지정", default=0)

# 데이터 1개당 반복학습할 횟수
parser.add_argument('--epochs', type=int, default=32)

# 몇개의 샘플당 가중치를 갱신할 것인지..
parser.add_argument('--batch_size', type=int, default=10)

# data가 1이면 학습 데이터셋 패스, 아니면 테스트 데이터셋 패스
parser.add_argument("--data", type=int, default=1)

# 입력받은 인자값 args에 저장(type: namespace)
config = parser.parse_args()

# 인자값 테스트
# print(config.caption_file_path)
# print(config.image_file_path)

```

- 세팅 값 저장

```python
def save_config(args):
    data = dict()
    # 데이터 생성
    # 캡션 파일경로
    data["caption_file_path"] = args.caption_file_path
    data["image_file_path"] = args.image_file_path
    data["do_sampling"] = args.do_sampling
    data["epochs"] = args.epochs
    data["batch_size"] = args.batch_size
    data["data"] = args.data

    with open('.\\settings.json', 'a', encoding='utf-8') as make_file:
        json.dump(data, make_file, indent="\t")
```

### 🔎이미지 캡셔닝 데이터 전처리

- 이미지 경로 및 캡션 불러오기

```python
def get_path_caption():
    img_paths = '.\\datasets\\images'
    csv_data = np.loadtxt('.\\datasets\\images\\results.csv',
                          delimiter='|', dtype="str", encoding="ISO-8859-1")

    # csv_data[i][0] : image_name
    # csv_data[i][1] : comment_number
    # csv_data[i][2] : comment

    # img_data[0] : 경로
    # img_data[1]: comment 1
    # img_data[2]: comment 2
    # img_data[3]: comment 3
    # img_data[4]: comment 4
    # img_data[5]: comment 5
    img_data = ['', '', '', '', '', '']
    captions = []

    for i in range(1, len(csv_data), 5):
        img_data[0] = img_paths + '\\' + csv_data[i][0]
        img_data[1] = csv_data[i][2]
        img_data[2] = csv_data[i+1][2]
        img_data[3] = csv_data[i+2][2]
        img_data[4] = csv_data[i+3][2]
        img_data[5] = csv_data[i+4][2]
        captions.append(img_data[:])
    return img_paths, captions
```

- 전체 데이터셋을 분리해 저장

```python
def dataset_split_save(captions):
    # caption : 158916 rows...
    train_dataset = []
    test_dataset = []

    # 1~5번 comment중 랜덤으로 학습,테스트용으로 나누기
    for i in range(len(captions)):
        num = random.randint(1, 5)
        if num < 2:
            train_dataset.append(captions[i])
        else:
            test_dataset.append(captions[i])

    # csvfile 오픈..
    # url, 파일 모드, 인코딩 타입 주의
    # 참고 링크 : https://m.blog.naver.com/PostView.nhn?blogId=real_77&logNo=221224637207&proxyReferer=https%3A%2F%2Fwww.google.com%2F
    csvfile = open(".\\datasets\\train_dataset.csv",
                   "w", newline="", encoding="utf-8")
    csvwriter = csv.writer(csvfile, quotechar="|", delimiter="|")

    for row in test_dataset:
        csvwriter.writerow(row)
    csvfile.close
    return ".\\datasets\\train_dataset.csv", ".\\datasets\\test_dataset_path"
```

- 저장된 데이터셋 불러오기

```python
def get_data_file(data, train_dataset_path, test_dataset_path):
    # data : parser.add_argument("--data", type=int, default=1)
    # train_dataset_path : 분리된 학습 데이터셋 경로
    # test_dataset_path : 분리된 테스트 데이터 경로

    # data가 1이면 학습 데이터셋 패스, 아니면 테스트 데이터셋 패스
    if data == 1:
        caption = np.loadtxt(train_dataset_path,
                             delimiter='|', dtype="str", encoding="UTF8")
        img_paths = caption[:, 0]
    else:
        caption = np.loadtxt(test_dataset_path, delimiter='|',
                             dtype="str", encoding="UTF8")
        img_path = caption[:, 0]

    return img_paths, caption
```

- 데이터 샘플링

```python
def sampling_data(img_paths, caption, sampling_count):
    if sampling_count > 10:
        return img_paths, caption
    cal_img_paths = []
    cal_csv_data = []

    for i in random.sample(list(range(len(caption))), sampling_count):
        cal_img_paths.append(caption[i][0])
        cal_csv_data.append(caption[i][1:6].tolist())
    return cal_img_paths, cal_csv_data
```

### 🔎데이터 시각화

- .png 파일 처리하기 위해 `plt.imshow()` 사용
  1. 가상 환경 라이브러리 설치
  ```bash
  conda install pillow
  ```
  2. 해당 py파일에 라이브러리 임포트
  ```python
  imgs = img.imread(img_paths[0])
  plt.title(caption[0][0])
  plt.imshow(imgs)
  plt.show()
  ```

## 😂프로젝트 수행 시 어려웠던 점

- python 문법에 익숙하지 않아, 적응하는 데 오래 걸렸다.<br/>
  (텐서플로 문서나, 다른 레퍼를 찾는데 문법마저 헷갈리니,,, 멘붕의 연속,,)

- 개인적으로도 공부해야할 양들이 많은 것같다.
- 딥러닝이 쓰이는 순서는 크게는 알겠지만, 부분마다 세밀한 로직을 파악하는 데 어려웠다.
- 모든 모델의 가장 기본이 되는 선형 회귀 모델을 증명하는 과정을 듣고 나니, 한결 나았다.
- 개인적인 공부를 하는 도중에, **중간중간 짧은 스크럼을 통해 팀원들과 공부 내용을 공유했다. (매우 중요한듯..)**
- 아직도 갈길은 멀지만, 큰 뼈대에 살을 붙이는 방법으로 조금씩 공부하자!!

## 📄참고

- [인공지능](https://brunch.co.kr/@gdhan/1)
- [머신러닝](https://swalloow.github.io/pyml-introl)

- [머신러닝](https://tykimos.github.io/2019/01/06/2018_ML_projects/)

- [딥러닝](https://brunch.co.kr/2itschloel/23)

- [뉴럴 네트워크 - 신경망의 구조](https://www.youtube.com/watch?v=aircAruvnKk)

- [경사하강법](https://www.youtube.com/watch?v=IHZwWFHWa-w)

- [역전파의 개념](https://www.youtube.com/watch?v=Ilg3gGewQ5U)

- [손실함수 - 대표적인 종류](https://eehoeskrap.tistory.com/145)

- [손실함수 - 크로스 엔트로피 함수](https://www.youtube.com/watch?v=uMYhthKw1PU)

- [파이썬 문법](https://wikidocs.net/22)
- [json 파일 저장](http://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221540272941)
- [argparse 모듈 문서](https://docs.python.org/ko/3.7/library/argparse.html)
- [csv 파일 저장 관련(pandas)](https://hogni.tistory.com/10)
- [파이썬 csv객체](https://m.blog.naver.com/PostView.nhn?blogId=real_77&logNo=221224637207&proxyReferer=https%3A%2F%2Fwww.google.com%2F)
