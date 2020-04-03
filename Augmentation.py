from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np


def do(img_tensor):
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    img_tensor = np.squeeze(img_tensor, axis=0)
    x = img_tensor  # (3, 150, 150) 크기의 NumPy 배열
    x = x.reshape((1,) + x.shape)  # (1, 3, 150, 150) 크기의 NumPy 배열

    datagen.flow()
