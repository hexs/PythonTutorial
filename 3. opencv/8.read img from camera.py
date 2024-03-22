import cv2

cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 5000)
while True:
    _, img = cap.read()
    print(img.shape)
    img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)
    cv2.imshow("display", img)
    cv2.waitKey(1)
