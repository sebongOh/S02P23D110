# 이미지 캡셔닝 기능 구현

<table>
   <tr>
      <td>
        <img width="160px" src="https://user-images.githubusercontent.com/58671945/78890548-d085b100-7aa0-11ea-9723-b146362f6dc5.jpg"><br>
         임현수<br>
         <i>Project dev & Front Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
      <td>
        <img width="160px" src="https://user-images.githubusercontent.com/58671945/78890552-d1b6de00-7aa0-11ea-85af-76bce9309754.jpg"><br>
         문준호<br>
         <i>Project dev & Front Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
      <td>
        <img width="160px" src="https://lab.ssafy.com/webmobile1-sub1/s02p11d138/raw/develop/KakaoTalk_20200109_090135135.jpg"><br>
         홍성욱<br>
         <i>Project Lead & Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
      <td>
        <img width="160px" src="https://user-images.githubusercontent.com/58671945/78890557-d380a180-7aa0-11ea-9d6d-2fef84900de9.jpg"><br>
         오세봉<br>
         <i>Project dev & Back Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
      <td>
        <img width="160px" src="https://user-images.githubusercontent.com/58671945/78890559-d4b1ce80-7aa0-11ea-80a2-6231f6a8f1ed.jpg"><br>
         박찬환<br>
         <i>Project dev & Back Developer</i><br>
         <i>SSAFY 2기 교육생</i>
      </td>
   </tr>
</table>

## 🤲 OverView<br> 

## ✨ Prequuisited<br>





### develop machine Spec

>- Gitlab - SSAFY gitlab 사용합니다. 문제 발생시 [gitLab docs](https://lab.ssafy.com/help)를 활용합니다.
>- Vue.js - VS Code 설치 및 [Vue.js 공식 웹사이트](https://kr.vuejs.org/index.html) 및 [StackOverflow](https://stackoverflow.com/)를 통해 시작합니다
>- Jira - [SSAFY jira](https://jira.ssafy.com/secure/Dashboard.jspa)를 사용합니다. jira를 통해 issue 및 WorkFlow 등 전반적인 스프린트를 관리합니다.
>- MySQL
>- django





## 🥨Commit/Branch Rules

### Commit

 #### Commit Message 7 Rules

> 1. 제목과 본문을 한 줄 띄워 분리하기
> 2. 제목은 영문 기준 50자 이내로
> 3. 제목 첫글자를 대문자로
> 4. 제목 끝에 . 금지
> 5. 제목은 명령조로
> 6. 본문은 영문 기준 72자마다 줄 바꾸기
> 7. 본문은 어떻게보다 무엇을, 왜에 맞춰 작성하기

 #### 단어 목록

> ##### 기본적으로 [타입] "무엇을" + "왜" 형식으로 관리
>
> 1. 수정 :: fix
>
> ```
> //비정상적 동작일 때, 
> //버그 잡을 때,
> [Fix] "무엇을" + ("왜")
> ```

> 2. 수정 :: update
>
> ```
> //정상적으로 동작할 때, 수정,추가,보완할 때
> [Update] "무엇을" + ("왜")
> ```

> 3. 추가 :: add
>
> ```
> [Add] "무엇을" + ("왜")
> ```

> 4. 삭제 :: remove
>
> ```
> [Remove] "무엇을" + ("왜")
> ```

> 5. 전면 수정 :: refactor
>
> ```
> [Refactor] "무엇을" + ("왜")
> ```

### Branch Naming (브랜치 명명 규칙)

> ##### > Gitlab에는 master와 develop 브랜치, 그리고 master 브랜치의 TAG만 관리한다.

> #### 개발자 PC
>
> 개발자는 PC에 release, hotfix, feature, issue 브랜치를 생성하여 작업을 진행한다.
> 작업이 완료된 브랜치는 병합후 삭제 가능하며, Gitlab에 반영하지 않는다.

> #### release 브랜치
>
> - develop 브랜치로부터 생성하는 브랜치이다.
> - 명명 규칙 : release/버젼넘버
>   ex) `release/2.0.0`
> - 브랜치 생성 후에는 버그 픽스만 반영한다.
> - 최종 확정 후에는 develop, master 브랜치에 병합한다.

> #### feature 브랜치
>
> - develop 브랜치로부터 생성하는 브랜치이다.
> - 명명 규칙 : 년월일_feature_짧은설명
>   ex) `200207_feature_BoardTransition`
> - 완료 후 develop 브랜치에 병합한다.



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
  

## Req. 1 이미지 데이터 전처리

### Req. 1-1 이미지 파일 로드

preprocess.py의 get_path_caption함수로 

train_dataset.csv, test_dataset.csv에서 데이터정보를 받아온 뒤,

img_preprocess.py의 img_pre함수로 각 이미지 경로를 불러온다.

### Req. 1-2 이미지 정규화

img_preprocess.py의 img_pre함수에서 이미지경로와 캡션을 각각 묶어서 저장한다.

train_test_split으로 학습할 데이터, 테스트할 데이터를 나눈다

```python
img_name_train, img_name_val, cap_train, cap_val = train_test_split(
    img_name_vector, cap_vector, test_size=0.2, random_state=0)
```



## Req. 2 텍스트 데이터 전처리

### Req. 2-1 텍스트 데이터 토큰화

my_token,py의 tokenization함수에서 캡션에 대한 데이터를 숫자데이터로 토큰화한뒤 리턴한다.

### Req. 2-2 Tokenizer 저장 및 불러오기

my_token,py의 Save_Tokenizer에서 토큰 저장을, Load_Tokenizer에서 토큰을 불러온다



## Req. 3 Dataset 생성 함수 구현

### Req. 3-1 tf.data.Dataset 생성

pre_trained_model.py의 Pre_trained_img함수에서 받아온 이미지 경로를 통하여 tf.data.Dataset을 생성한다.

```python
encode_train = sorted(set(img_name_vector))
    image_dataset = tf.data.Dataset.from_tensor_slices(encode_train)
    image_dataset = image_dataset.map(
                            load_image, num_parallel_calls=tf.data.experimental.AUTOTUNE).batch(16)
    image_model = tf.keras.applications.InceptionV3(include_top=False,
                                                    weights='imagenet')
```



### Req. 3-2 Image Data Augmentation

img_preprocess.py의 img_pre에서 각 이미지를 변형한다

```python
    datagen = image.ImageDataGenerator(
        rotation_range=5,
        width_shift_range=0.1,
        height_shift_range=0.1,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.12,
        horizontal_flip=True,
        fill_mode='nearest')
```



## Req. 4 이미지 모델 구현

### Req. 4-1 Pre-trained 모델로 특성 추출

pre-trained 모델 : Inception, VGG, MobileNet, NASNet 등

InceptionV3모델을 사용

Augumentation : 같은 사진을 쓰더라도 기울이거나 자르거나 뒤집어서 학습할 자료를 추가로 생성

ImageDataGenerator 를 사용해서 한 이미지당 여러가지의 자료를 생성한다. 

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

image = load_img('bird_resize.jpg', target_size=(220,200))
image = img_to_array(image)
image = image.reshape((1,) + image.shape)
i = 0
for batch in datagen.flow(image, batch_size=1,
                          save_to_dir='preview', save_prefix='bird', save_format='jpeg'):
    i += 1
    if i > 30:
        break  # 이미지 30개 생성
```

각 변수 참고자료 : https://keras.io/preprocessing/image/

### Red. 4-2 Feature Encoder 구현

이미지 크기를

220x200x3 - 220x200x64 - 110x100x128 - 55x50x256 - 27x25x512 - 13x12x512 순서로 Encoding

glob : 폴더 내의 특정 파일명만 모아줌





## Req. 5 텍스트 모델 구현

### Req. 5-1 임베딩 레이어 구현

토큰화된 벡터를 지정한 공간에 투영

```
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)

```



### Req. 5-2 RNN 모델 구현

임베인 된 벡터를 입력으로 받는 RNN 모델을 구현

```
        self.gru = tf.keras.layers.GRU(self.units,
                                       return_sequences=True,
                                       return_state=True,
                                       recurrent_initializer='glorot_uniform')
```



### Req. 5-3 역임베딩 레이어 구현

결과값을 토큰화 된 정답 데이터와 비교 가능하게 차원을 변형

```
        self.fc1 = tf.keras.layers.Dense(self.units)
        self.fc2 = tf.keras.layers.Dense(vocab_size)
```



## Req. 6 train.py 구현

### Req. 6-1 손실 함수 구현
예측값과 정답값을 입력으로 받아 손실을 계산하는 함수를 구현

```
        features = encoder(img_tensor)

        for i in range(1, target.shape[1]):
            predictions, hidden, _ = decoder(dec_input, features, hidden)

            loss += loss_function(target[:, i], predictions)

            dec_input = tf.expand_dims(target[:, i], 1)
```

### Req. 6-2 1-batch train step 구현
배치 데이터를 입력받아 손실을 계산하고 모델을 학습하는 함수 구현

```
    with tf.GradientTape() as tape:
total_loss = (loss / int(target.shape[1]))

    trainable_variables = encoder.trainable_variables + decoder.trainable_variables

    gradients = tape.gradient(loss, trainable_variables)
```



### Req. 6-3 train.py 완성
여기까지 구현된 전처리, 모델, 최적화함수및 손실함수를 이용하여 모델을 학습시키는 과정 구현

```
BATCH_SIZE = 2048

EPOCHS = 30
num_steps = len(img_name_train) // BATCH_SIZE

for epoch in range(start_epoch, EPOCHS):
    start = time.time()
    total_loss = 0

    for (batch, (img_tensor, target)) in enumerate(dataset):
        batch_loss, t_loss = pre_trained_model.train_step(img_tensor, target, encoder, decoder, tokenizer, optimizer)
        total_loss += t_loss

        if batch % 100 == 0:
            print ('Epoch {} Batch {} Loss {:.4f}'.format(
                epoch + 1, batch, batch_loss.numpy() / int(target.shape[1])))
    # storing the epoch end loss value to plot later
    loss_plot.append(total_loss / num_steps)

    if epoch % 5 == 0:
        ckpt_manager.save()

    print ('Epoch {} Loss {:.6f}'.format(epoch + 1,
                                         total_loss/num_steps))
    print ('Time taken for 1 epoch {} sec\n'.format(time.time() - start))


```





## Req. 7 predict.py 구현



### Req. 7-1 캡션 생성 함수 구현
캡션 문장을 생성하는 함수를 구현

```
rid = np.random.randint(0, len(img_name_val))
image = img_name_val[rid]
real_caption = ' '.join([tokenizer.index_word[i] for i in cap_val[rid] if i not in [0]])
result, attention_plot = pre_trained_model.evaluate(image, max_length, attention_features_shape, encoder, decoder, pre_trained_model, image_features_extract_model, tokenizer)

print ('Real Caption:', real_caption)
print ('Prediction Caption:', ' '.join(result))
pre_trained_model.plot_attention(image, result, attention_plot)

```



### Req. 7-2 predict.py 구현

랜덤한 이미지를 넣어서 실제값과 예측값을 비교하는 과정 구현

```
def plot_attention(image, result, attention_plot):
    temp_image = np.array(Image.open(image))

    fig = plt.figure(figsize=(10, 10))

    len_result = len(result)
    for l in range(len_result):
        temp_att = np.resize(attention_plot[l], (8, 8))
        ax = fig.add_subplot(len_result//2, len_result//2, l+1)
        ax.set_title(result[l])
        img = ax.imshow(temp_image)
        ax.imshow(temp_att, cmap='gray', alpha=0.6, extent=img.get_extent())

    plt.tight_layout()
    plt.show()
```



## Req. 8 체크포인트 매니저



### Req. 8-1 체크포인트 생성 및 저장 함수 구현
CheckpointManager를 이용하여 모델의 변수들을 저장

```
checkpoint_path = "./checkpoints/train"
ckpt = tf.train.Checkpoint(encoder=encoder,
                           decoder=decoder,
                           optimizer = optimizer)
ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

start_epoch = 0
```



### Req. 8-2 체크포인트 로더 구현
checkpoints/train에 저장된 체크포인트 파일을 불러올 로더를 구현

```
if ckpt_manager.latest_checkpoint:
    start_epoch = int(ckpt_manager.latest_checkpoint.split('-')[-1])
    # restoring the latest checkpoint in checkpoint_path
    ckpt.restore(ckpt_manager.latest_checkpoint)

```




