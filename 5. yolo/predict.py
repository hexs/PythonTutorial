from hexss import check_packages

check_packages(
    'ultralytics', 'opencv-python',
    auto_install=True, verbose=False,
)

import cv2
from ultralytics import YOLO

model = YOLO(r'fine-a-red-hat\runs\detect\train\weights\best.pt')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame)

        annotated_frame = results[0].plot()

        cv2.imshow("YOLOv8 Inference", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
