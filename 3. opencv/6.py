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
# start_pos = Point(0, 0)
# stop_pos = Point(0, 0)
# drawing = False
#
#
# def click_event(event, x, y, flags, params):
#     global pos, start_pos, stop_pos, drawing
#     pos = Point(x, y)
#     if event == cv2.EVENT_LBUTTONDOWN:
#         start_pos = Point(x, y)
#         drawing = True
#     elif event == cv2.EVENT_LBUTTONUP:
#         stop_pos = Point(x, y)
#         drawing = False
#     elif event == cv2.EVENT_MOUSEMOVE and drawing:
#         pos = Point(x, y)
#
#
# r = []
# r.append(Rect(Point(100, 200), Point(300, 400)))
# while True:
#     img = cv2.imread('img.png')
#     r0 = Rect(start_pos, stop_pos)
#     r0.show(img, (255, 0, 0))
#     for i in r:
#         i.show(img, (255, 0, 0))
#
#     cv2.putText(img, f'pos {pos.x, pos.y}', [10, 50], 1, 3, (0, 0, 255), 2, cv2.LINE_AA)
#     cv2.circle(img, pos.xy, 30, (0, 0, 255), -1)
#     cv2.imshow('img', img)
#     cv2.setMouseCallback('img', click_event)
#     k = cv2.waitKey(1)
#     if k == ord('a'):
#         r.append(r0)
#     if k == ord('s'):
#         rect_lst = []
#         for i in r:
#             print(i)
#             rect_lst.append(i.xyxy())
#         print(rect_lst)
