import os
import random

from hexss import check_packages

check_packages(
    'ultralytics', 'opencv-python',
    auto_install=True, verbose=False,
)

import cv2
from ultralytics import YOLO

model = YOLO('fine-a-red-hat/runs/detect/train/weights/best.pt')

image_list = os.listdir('fine-a-red-hat/datasets/test/images')
image_name = random.choice(image_list)

img = cv2.imread(os.path.join('fine-a-red-hat/datasets/test/images', image_name))

results = model(img)

annotated_frame = results[0].plot()

cv2.imshow("YOLOv8 Inference", cv2.resize(annotated_frame, None, fx=0.8, fy=0.8))
cv2.waitKey(0)


# cap = cv2.VideoCapture(0)
# while cap.isOpened():
#     _, frame = cap.read()
#
#     results = model(frame)
#
#     annotated_frame = results[0].plot()
#
#     cv2.imshow("YOLOv8 Inference", annotated_frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
