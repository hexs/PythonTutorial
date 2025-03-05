import cv2

pos = None


def click_event(event, x, y, flags, params):
    global pos
    pos = x, y
    print(pos)


while True:
    img = cv2.imread('img.png')
    cv2.putText(img, f'pos {pos}', [10, 50], 1, 3, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('img', img)
    cv2.setMouseCallback('img', click_event)
    cv2.waitKey(1)
