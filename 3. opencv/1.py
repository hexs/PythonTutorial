from hexss import check_packages

check_packages(
    'opencv-python',
    auto_install=True,
)

import numpy as np
import cv2

img = np.array(
    # B G R
    [
        [[000, 000, 000], [255, 255, 255], [127, 127, 127]],
        [[255, 000, 000], [000, 255, 000], [000, 000, 255]],
        [[000, 255, 255], [255, 000, 255], [255, 255, 000]]
    ]
    , dtype=np.uint8)

img = cv2.resize(img, (0, 0), fx=100, fy=100, interpolation=0)
cv2.imshow('img', img)
cv2.waitKey(0)
