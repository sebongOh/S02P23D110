import tensorflow as tf
import numpy as np
import time
import matplotlib.pyplot as plt
from PIL import Image

from data import preprocess
from sklearn.model_selection import train_test_split  # 데이터를 학습용/테스트용으로  분리해주는 유틸리티
import my_token
import img_preprocess
import img_extract
import create
import CNN
import RNN
import pre_trained_model

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
# if(my_token.Load_Tokenizer() == None):
#     print("dddddddddddddddddddddd")
tokenizer, cap_vector, train_seqs, max_length = my_token.tokenization(
    train_captions[: my_token.top_k * 5]
)
#     my_token.Save_Tokenizer(my_tokenizer)
#     my_token.Save_Captions(cap_vector)
#     my_token.Save_Seqs(train_seqs)
#     tokenizer = my_token.Load_Tokenizer()
#     cap_vector = my_token.Load_Captions()
#     train_seqs = my_token.Load_Seqs()
# else:
#     tokenizer = my_token.Load_Tokenizer()
#     cap_vector = my_token.Load_Captions()
#     train_seqs = my_token.Load_Seqs()

# ===========================================


# ==================
# 토크나이저 저장하기
# my_token.Save_Tokenizer(my_tokenizer)
# # 토크나이저 불러오기
# my_tokenizer = my_token.Load_Tokenizer()
# ==================


# =============================
# 학습/테스트용 데이터로 분할하기
# (학습용 80% / 테스트용 20%로 설정)
# test_size가 0.2이면 train_size는 0.8
# 따라서 train:test = 80% : 20%
img_name_train, img_name_val, cap_train, cap_val = train_test_split(
    img_name_vector, cap_vector, test_size=0.2, random_state=0
)
# ====================-=======


# # tf 데이터셋 만들기
dataset = create.create_tf_data(tokenizer, img_name_train, cap_train)


# 환경 변수
embedding_dim = 256
units = 512
vocab_size = my_token.top_k + 1

# 모델 학습
encoder = CNN.CNN_Encoder(embedding_dim)
decoder = RNN.RNN_Decoder(embedding_dim, units, vocab_size)

print(encoder, decoder)

image_features_extract_model = pre_trained_model.Pre_trained_img(img_name_vector)



# Find the maximum length of any caption in our dataset

# # Choose the top 5000 words from the vocabulary
# tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=my_token.top_k,
#                                                   oov_token="<unk>",
#                                                   filters='!"#$%&()*+.,-/:;=?@[\]^_`{|}~ ')
# tokenizer.fit_on_texts(train_captions)
# train_seqs = tokenizer.texts_to_sequences(train_captions)


# tokenizer.word_index['<pad>'] = 0
# tokenizer.index_word[0] = '<pad>'


# # # Create the tokenized vectors
# # train_seqs = tokenizer.texts_to_sequences(train_captions)

# # # Pad each vector to the max_length of the captions
# # # If you do not provide a max_length value, pad_sequences calculates it automatically
# # cap_vector = tf.keras.preprocessing.sequence.pad_sequences(train_seqs, padding='post')

# # # Calculates the max_length, which is used to store the attention weights
# # max_length = calc_max_length(train_seqs)

# # # Create training and validation sets using an 80-20 split
# # img_name_train, img_name_val, cap_train, cap_val = train_test_split(img_name_vector,
# #                                                                     cap_vector,
# #                                                                     test_size=0.2,
# #                                                                     random_state=0)

# print(len(img_name_train), len(cap_train), len(img_name_val), len(cap_val))


class BahdanauAttention(tf.keras.Model):
    def __init__(self, units):
        super(BahdanauAttention, self).__init__()
        self.W1 = tf.keras.layers.Dense(units)
        self.W2 = tf.keras.layers.Dense(units)
        self.V = tf.keras.layers.Dense(1)

    def call(self, features, hidden):
        # features(CNN_encoder output) shape == (batch_size, 64, embedding_dim)

        # hidden shape == (batch_size, hidden_size)
        # hidden_with_time_axis shape == (batch_size, 1, hidden_size)
        hidden_with_time_axis = tf.expand_dims(hidden, 1)

        # score shape == (batch_size, 64, hidden_size)
        score = tf.nn.tanh(self.W1(features) + self.W2(hidden_with_time_axis))

        # attention_weights shape == (batch_size, 64, 1)
        # you get 1 at the last axis because you are applying score to self.V
        attention_weights = tf.nn.softmax(self.V(score), axis=1)

        # context_vector shape after sum == (batch_size, hidden_size)
        context_vector = attention_weights * features
        context_vector = tf.reduce_sum(context_vector, axis=1)

        return context_vector, attention_weights


optimizer = tf.keras.optimizers.Adam()
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(
    from_logits=True, reduction="none"
)


def loss_function(real, pred):
    mask = tf.math.logical_not(tf.math.equal(real, 0))
    loss_ = loss_object(real, pred)

    mask = tf.cast(mask, dtype=loss_.dtype)
    loss_ *= mask

    return tf.reduce_mean(loss_)


checkpoint_path = "./checkpoints/train"
ckpt = tf.train.Checkpoint(encoder=encoder, decoder=decoder, optimizer=optimizer)
ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

start_epoch = 0
if ckpt_manager.latest_checkpoint:
    start_epoch = int(ckpt_manager.latest_checkpoint.split('-')[-1])
    # restoring the latest checkpoint in checkpoint_path
    ckpt.restore(ckpt_manager.latest_checkpoint)

# adding this in a separate cell because if you run the training cell
# many times, the loss_plot array will be reset
loss_plot = []


@tf.function
def train_step(img_tensor, target):
    loss = 0

    # initializing the hidden state for each batch
    # because the captions are not related from image to image
    hidden = decoder.reset_state(batch_size=target.shape[0])

    dec_input = tf.expand_dims([tokenizer.word_index["<start>"]] * target.shape[0], 1)

    with tf.GradientTape() as tape:
        features = encoder(img_tensor)

        for i in range(1, target.shape[1]):
            # passing the features through the decoder
            predictions, hidden, _ = decoder(dec_input, features, hidden)

            loss += loss_function(target[:, i], predictions)

            # using teacher forcing
            dec_input = tf.expand_dims(target[:, i], 1)

    total_loss = loss / int(target.shape[1])

    trainable_variables = encoder.trainable_variables + decoder.trainable_variables

    gradients = tape.gradient(loss, trainable_variables)

    optimizer.apply_gradients(zip(gradients, trainable_variables))

    return loss, total_loss


print("학습을 시작합니다")
BATCH_SIZE = 64
BUFFER_SIZE = 1000

EPOCHS = 100
num_steps = len(img_name_train) // BATCH_SIZE

for epoch in range(start_epoch, EPOCHS):
    start = time.time()
    total_loss = 0

    for (batch, (img_tensor, target)) in enumerate(dataset):
        batch_loss, t_loss = train_step(img_tensor, target)
        total_loss += t_loss

        if batch % 100 == 0:
            print(
                "Epoch {} Batch {} Loss {:.4f}".format(
                    epoch + 1, batch, batch_loss.numpy() / int(target.shape[1])
                )
            )
    # storing the epoch end loss value to plot later
    loss_plot.append(total_loss / num_steps)

    if epoch % 5 == 0:
        ckpt_manager.save()

    print("Epoch {} Loss {:.6f}".format(epoch + 1, total_loss / num_steps))
    print("Time taken for 1 epoch {} sec\n".format(time.time() - start))

plt.plot(loss_plot)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Loss Plot")
plt.show()


def calc_max_length(tensor):
    return max(len(t) for t in tensor)


max_length = calc_max_length(train_seqs)

attention_features_shape = 64


def evaluate(image):
    attention_plot = np.zeros((max_length, attention_features_shape))

    hidden = decoder.reset_state(batch_size=1)

    temp_input = tf.expand_dims(pre_trained_model.load_image(image)[0], 0)
    img_tensor_val = image_features_extract_model(temp_input)
    img_tensor_val = tf.reshape(
        img_tensor_val, (img_tensor_val.shape[0], -1, img_tensor_val.shape[3])
    )

    features = encoder(img_tensor_val)

    dec_input = tf.expand_dims([tokenizer.word_index["<start>"]], 0)
    result = []

    for i in range(max_length):
        predictions, hidden, attention_weights = decoder(dec_input, features, hidden)

        attention_plot[i] = tf.reshape(attention_weights, (-1,)).numpy()

        predicted_id = tf.random.categorical(predictions, 1)[0][0].numpy()
        result.append(tokenizer.index_word[predicted_id])

        if tokenizer.index_word[predicted_id] == "<end>":
            return result, attention_plot

        dec_input = tf.expand_dims([predicted_id], 0)

    attention_plot = attention_plot[: len(result), :]
    return result, attention_plot


def plot_attention(image, result, attention_plot):
    temp_image = np.array(Image.open(image))

    fig = plt.figure(figsize=(10, 10))

    len_result = len(result)
    for l in range(len_result):
        temp_att = np.resize(attention_plot[l], (8, 8))
        ax = fig.add_subplot(len_result // 2, len_result // 2, l + 1)
        ax.set_title(result[l])
        img = ax.imshow(temp_image)
        ax.imshow(temp_att, cmap="gray", alpha=0.6, extent=img.get_extent())

    plt.tight_layout()
    plt.show()


# captions on the validation set
rid = np.random.randint(0, len(img_name_val))
image = img_name_val[rid]
real_caption = " ".join([tokenizer.index_word[i] for i in cap_val[rid] if i not in [0]])
result, attention_plot = evaluate(image)

print("Real Caption:", real_caption)
print("Prediction Caption:", " ".join(result))
plot_attention(image, result, attention_plot)

# image_url = 'https://tensorflow.org/images/surf.jpg'
# image_extension = image_url[-4:]
# image_path = tf.keras.utils.get_file('image'+image_extension,
#                                      origin=image_url)

# result, attention_plot = evaluate(image_path)
# print ('Prediction Caption:', ' '.join(result))
# plot_attention(image_path, result, attention_plot)
# # opening the image
# Image.open(image_path)
