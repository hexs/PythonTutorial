import json
from datetime import datetime
import cv2
import numpy as np
from data_file import ini_to_dict
from keras import models
from train import add_img, train, predict

cap = cv2.VideoCapture(0)
h_cap = 480
w_cap = 640


def xyxy_to_xywh(x1, y1, x2, y2):
    x1 = x1 / w_cap
    y1 = y1 / h_cap
    x2 = x2 / w_cap
    y2 = y2 / h_cap
    x = round((x1 + x2) / 2, 6)
    y = round((y1 + y2) / 2, 6)
    w = round(abs(x1 - x2), 6)
    h = round(abs(y1 - y2), 6)
    xywh = x, y, w, h
    return xywh


def xywh_to_xyxy(x, y, w, h):
    x = x * w_cap
    y = y * h_cap
    w = w * w_cap
    h = h * h_cap
    x1 = int(x - w / 2)
    y1 = int(y - h / 2)
    x2 = int(x + w / 2)
    y2 = int(y + h / 2)
    xyxy = x1, y1, x2, y2
    return xyxy


d = ini_to_dict('model_position.ini', True)
print((d))
for k, v in d.items():
    v['xyxy'] = xywh_to_xyxy(*v['pos'])
    v['x1y1'] = v['xyxy'][:2]
    v['x2y2'] = v['xyxy'][2:]
print(d)
model_name = 'm1'
while cap.isOpened():
    success, img = cap.read()
    if success:
        for i, v in enumerate(d[f'{model_name}']['status_list'], 1):
            cv2.putText(img, f'{i} {v}', (5, 20 * i), 1, 1, (255, 0, 0), 1)
        for k, v in d.items():
            cv2.rectangle(img, v['x1y1'], v['x2y2'], (255, 0, 0), 2)
            cv2.putText(img, f'{k}', v['x1y1'], 1, 1.5, (255, 0, 0), 2)
        cv2.imshow("img", img)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        if ord("1") <= key < ord("1") + len(d[f'{model_name}']['status_list']):
            class_list = d[f'{model_name}']['status_list'][int(chr(key)) - 1]
            x1, y1, x2, y2 = d[f'{model_name}']['xyxy']
            add_img(img, x1, y1, x2, y2, f'dataset/{class_list}')
            cv2.destroyAllWindows()
            train()

        if key == ord("0"):
            model = models.load_model('model_name.h5')
            x1, y1, x2, y2 = d[f'{model_name}']['xyxy']
            img = img[y1:y2, x1:x2]
            img = cv2.resize(img, (180, 180))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            with open('class_names.json') as f:
                class_name = json.loads(f.read())
            res = predict(model, img, class_name)
            print(res)
        if key == ord("."):
            cv2.destroyAllWindows()
            train()