import json
import os
import pathlib
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
from keras import models
import cv2


def controller(img, brightness=255, contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness
        al_pha = (max - shadow) / 255
        ga_mma = shadow
        cal = cv2.addWeighted(img, al_pha, img, 0, ga_mma)
    else:
        cal = img

    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
        cal = cv2.addWeighted(cal, Alpha, cal, 0, Gamma)
    return cal


def add_img(img, x1, y1, x2, y2, path):
    for shift_y in [0]:
        for shift_x in [0]:
            img_crop = img[y1 + shift_y:y2 + shift_y, x1 + shift_x:x2 + shift_x]

            brightness = [230, 242, 255, 267, 280]
            contrast = [114, 120, 127, 133, 140]
            for b in brightness:
                for c in contrast:
                    img_crop_BC = img_crop.copy()
                    img_crop_BC = controller(img_crop_BC, b, c)
                    namefile = datetime.now().strftime('%y%m%d %H%M%S')
                    img_crop_namefile = f'{namefile} {shift_y} {shift_x} {b} {c}.png'
                    cv2.imwrite(fr"{path}/{img_crop_namefile}", img_crop_BC)


def train():
    data_dir = pathlib.Path('dataset')

    batch_size = 32
    img_height = 180
    img_width = 180

    train_ds, val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="both",
        seed=123,
        image_size=(img_height, img_width),
        batch_size=batch_size)

    class_names = train_ds.class_names

    AUTOTUNE = tf.data.AUTOTUNE

    train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
    normalization_layer = layers.Rescaling(1. / 255)

    normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
    image_batch, labels_batch = next(iter(normalized_ds))
    first_image = image_batch[0]
    # Notice the pixel values are now in `[0,1]`.
    print(np.min(first_image), np.max(first_image))

    num_classes = len(class_names)

    model = Sequential([
        layers.RandomFlip("horizontal", input_shape=(img_height, img_width, 3)),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
        layers.Rescaling(1. / 255, input_shape=(img_height, img_width, 3)),
        layers.Conv2D(16, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(32, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, padding='same', activation='relu'),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes)
    ])
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    model.summary()

    epochs = 50
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=epochs
    )

    model.save(os.path.join('model_name.h5'))
    with open('class_names.json', 'w') as f:
        f.write(json.dumps(class_names))


def predict(model, img_array, class_name):
    img_array4 = np.expand_dims(img_array, axis=0)
    predictions = model.predict_on_batch(img_array4)
    exp_x = [2.7 ** x for x in predictions[0]]
    percent_score_list = [round(x * 100 / sum(exp_x)) for x in exp_x]
    highest_score_index = np.argmax(predictions[0])  # 3
    highest_score_name = class_name[highest_score_index]
    highest_score_percent = percent_score_list[highest_score_index]
    return highest_score_name, highest_score_percent


if __name__ == '__main__':
    model = models.load_model('model_name.h5')
    img = cv2.cvtColor(cv2.resize(cv2.imread('1.jpg'), (180, 180)), cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, axis=0)
    with open('class_names.json') as f:
        class_name = json.loads(f.read())

    res = predict(model, img, class_name)
    print(res)
