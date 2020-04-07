import tensorflow as tf


def load_image(image_path):
    result_img = []
    for i in image_path:

        img = tf.io.read_file(i)
        img = tf.image.decode_jpeg(img, channels=3)
        img = tf.image.resize(img, (299, 299))
        img = tf.keras.applications.inception_v3.preprocess_input(img)
        # 이미지 크기 조절
        # preprocess_input메소드가 이미지를 정규화 시켜줌
        result_img.append(img)
    return result_img, image_path
