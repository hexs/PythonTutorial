import numpy as np
import cv2

img = np.array(
    # B G R
    [
        [[000, 000, 000], [255, 255, 255], [127, 127, 127], [255, 255, 255], [000, 000, 000]],
        [[255, 000, 000], [000, 255, 000], [000, 000, 255], [000, 255, 000], [255, 000, 000]],
        [[000, 255, 255], [255, 000, 255], [255, 255, 000], [255, 000, 255], [000, 255, 255]],
        [[000, 000, 000], [255, 255, 255], [127, 127, 127], [255, 255, 255], [000, 000, 000]],
    ]
    , dtype=np.uint8)
img_resize = cv2.resize(img, (0, 0), fx=50, fy=50, interpolation=0)
cv2.imshow('img', img_resize)
print(img.shape)
cv2.waitKey(0)


img2 = np.full([400, 400, 3], [100,100,100],np.uint8)
print(img2.shape)
cv2.imshow('img2', img2)
cv2.waitKey(0)
