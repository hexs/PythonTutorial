import random
from hexss import check_packages

check_packages(
    'opencv-python', 'cvzone',
    auto_install=True,
)

import cv2
import cvzone
import numpy as np

# Initialize camera capture
cap = cv2.VideoCapture(0)

r = 0
g = 0
b = 0
img2 = cv2.imread('img.png', cv2.IMREAD_UNCHANGED)
print(img2.shape)
img2 = cv2.resize(img2, (300, 300))
while True:
    r = min(255, max(0, int(random.randint(r - 3, r + 3))))
    g = min(255, max(0, int(random.randint(g - 3, g + 3))))
    b = min(255, max(0, int(random.randint(b - 3, b + 3))))

    display = np.full((900, 900, 3), (b, g, r), np.uint8)
    success, img = cap.read()
    img = cv2.resize(img, (500, 500))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    cvzone.overlayPNG(display, img, (100, 100))
    cvzone.overlayPNG(display, img2, (500, 500))
    cv2.imshow("display", display)
    cv2.waitKey(1)
