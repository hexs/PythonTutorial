import json
from hexss import check_packages

check_packages(
    'tensorflow', 'opencv-python',
    auto_install=True, verbose=False,
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
with open('class_names.json') as f:
    class_name = json.loads(f.read())

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, img = cap.read()
    if success:
        imgresize = cv2.resize(img, (180, 180))
        imgresize = np.expand_dims(imgresize, axis=0)
        res = predict(model, imgresize, class_name)
        print(res)
        cv2.imshow("img", img)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
