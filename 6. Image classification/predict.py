"https://poloclub.github.io/cnn-explainer/"
from hexss import check_packages, json_load

check_packages(
    'tensorflow', 'opencv-python',
    auto_install=True,
)

import cv2
import numpy as np
from keras import models


def predict(model, img_array, class_name):
    predictions = model.predict_on_batch(img_array)
    exp_x = [2.7 ** x for x in predictions[0]]
    percent_score_list = [round(x * 100 / sum(exp_x)) for x in exp_x]
    highest_score_index = np.argmax(predictions[0])
    highest_score_name = class_name[highest_score_index]
    highest_score_percent = percent_score_list[highest_score_index]
    return highest_score_name, highest_score_percent


model = models.load_model('model_name.h5')
class_names = json_load('class_names.json')['class_names']

img = cv2.imread('flower_photos/sunflowers/44079668_34dfee3da1_n.jpg')
img = cv2.cvtColor(cv2.resize(img, (180, 180)), cv2.COLOR_BGR2RGB)
img = np.expand_dims(img, axis=0)

res = predict(model, img, class_names)
print(res)
