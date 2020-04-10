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

```
        features = encoder(img_tensor)

        for i in range(1, target.shape[1]):
            predictions, hidden, _ = decoder(dec_input, features, hidden)

            loss += loss_function(target[:, i], predictions)

            dec_input = tf.expand_dims(target[:, i], 1)
```

### Req. 6-2 1-batch train step 구현

```
    with tf.GradientTape() as tape:
total_loss = (loss / int(target.shape[1]))

    trainable_variables = encoder.trainable_variables + decoder.trainable_variables

    gradients = tape.gradient(loss, trainable_variables)
```



### Req. 6-3 train.py 완성

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

```
checkpoint_path = "./checkpoints/train"
ckpt = tf.train.Checkpoint(encoder=encoder,
                           decoder=decoder,
                           optimizer = optimizer)
ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

start_epoch = 0
```



### Req. 8-2 체크포인트 로더 구현

```
if ckpt_manager.latest_checkpoint:
    start_epoch = int(ckpt_manager.latest_checkpoint.split('-')[-1])
    # restoring the latest checkpoint in checkpoint_path
    ckpt.restore(ckpt_manager.latest_checkpoint)

```



## 실행 결과



