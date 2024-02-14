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

img_resize = cv2.resize(img, (0, 0), fx=100, fy=100, interpolation=0)
cv2.imshow('old', img_resize)

img[0, 0] = [255, 255, 255]
img_resize = cv2.resize(img, (0, 0), fx=100, fy=100, interpolation=0)
cv2.imshow('new', img_resize)

img[1, 0] = [255, 255, 255]
img_resize = cv2.resize(img, (0, 0), fx=100, fy=100, interpolation=0)
cv2.imshow('new new', img_resize)

cv2.waitKey(0)
