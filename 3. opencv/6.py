import cv2

pos = (0, 0)


def click_event(event, x, y, flags, params):
    global pos
    pos = x, y


while True:
    img = cv2.imread('img.png')
    x1y1 = (100, 200)
    x2y2 = (300, 400)

    cv2.rectangle(img, x1y1, x2y2, (255, 0, 0), 2)  # กรอบน้ำเงิน

    if x1y1[0] < pos[0] < x2y2[0] and x1y1[1] < pos[1] < x2y2[1]:
        cv2.rectangle(img, x1y1, x2y2, (0, 255, 0), 2)  # กรอบเขียว

    cv2.putText(img, f'pos {pos}', [10, 50], 1, 3, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.circle(img, pos, 30, (0, 0, 255), -1)
    cv2.imshow('img', img)
    cv2.setMouseCallback('img', click_event)
    cv2.waitKey(1)

# todo
#  ไปดู ข้อ 7 ก่อน

# import cv2
# from Rect import Point, Rect
#
# pos = Point(0, 0)
#
#
# def click_event(event, x, y, flags, params):
#     global pos
#     pos = Point(x, y)
#
#
# while True:
#     img = cv2.imread('img.png')
#     r1 = Rect(Point(100, 200), Point(300, 400))
#
#     cv2.rectangle(img, list(r1.p1), list(r1.p2), (255, 0, 0), 2)  # กรอบน้ำเงิน
#     if r1.has_point_on_it(pos):
#         cv2.rectangle(img, list(r1.p1), list(r1.p2), (0, 255, 0), 2)  # กรอบเขียว
#
#     cv2.putText(img, f'pos {pos.x, pos.y}', [10, 50], 1, 3, (0, 0, 255), 2, cv2.LINE_AA)
#     cv2.circle(img, list(pos), 30, (0, 0, 255), -1)
#     cv2.imshow('img', img)
#     cv2.setMouseCallback('img', click_event)
#     cv2.waitKey(1)
