import random
import json
from hexss import check_packages

check_packages(
    'opencv-python' 'mediapipe', 'cvzone',
    auto_install=True, verbose=False,
)

import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2
from Rect import Point, Rect

pos = Point(0, 0)
start_pos = Point(0, 0)
stop_pos = Point(0, 0)
dwg = False
hand_have = ''
parts = {'p1': '-', 'p2': '-', 'p3': '-'}


def click_event(event, x, y, flags, params):
    global pos, start_pos, stop_pos, dwg
    # pos = Point(x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        start_pos = Point(x, y)
        stop_pos = Point(x, y)
        dwg = True
    if event == cv2.EVENT_LBUTTONUP:
        stop_pos = Point(x, y)
        dwg = False
    if event == cv2.EVENT_MOUSEMOVE and dwg == True:
        stop_pos = Point(x, y)


rects = {}
try:
    with open("datasave.json", "r") as f:  # Read
        string = f.read()
    dct = json.loads(string)
    for k, v in dct.items():
        name = k
        x1, y1, x2, y2 = v
        rects[name] = Rect(name, Point(x1, y1), Point(x2, y2))
except:
    pass

cap = cv2.VideoCapture(0)
detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
while True:
    success, img = cap.read()
    img = cv2.resize(img, (0, 0), fx=1.5, fy=1.5)

    r1 = Rect('-', start_pos, stop_pos)
    for rect in rects.values():
        rect.show(img, pos)
    r1.show(img, pos)

    hands, img = detector.findHands(img, draw=True, flipType=True)

    hand_right = None
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

        if handType1 == "Right":
            hand_right = lmList1

        if len(hands) == 2:
            # Information for the second hand
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]

            if handType2 == "Right":
                hand_right = lmList1

    if hand_right:
        x, y, z = hand_right[12]
        pos = Point(x, y)
    else:
        pos = Point(0, 0)

    for k, v in rects.items():
        if v.has_point_on_it(pos):
            if k != 'main':
                hand_have = k

    if hand_have:
        if rects['main'].has_point_on_it(pos):
            parts[hand_have] = 'ok'
            hand_have = ''

    cvzone.putTextRect(img, f'hand have {hand_have}', (10, 30), 2, 2, (0, 0, 0), (255, 255, 255), offset=8)
    for i, (k, v) in enumerate(parts.items()):
        cvzone.putTextRect(img, f'{k} {v}', (10, 65 + 35 * i), 2, 2, (0, 0, 0), (255, 255, 255), offset=8)

    cv2.imshow("Image", img)
    cv2.setMouseCallback('Image', click_event)
    key = cv2.waitKey(1)
    if key == -1:
        continue
    print(key)
    if key == ord("a"):
        name = ''
        for i in range(5):
            name += random.choice('abcdefghijklmnopqrqtuvwxyz')
        r1.name = name
        rects[name] = r1

        lts = {}
        for rect in rects.values():
            lts[rect.name] = rect.xyxy()
        string = json.dumps(lts, indent=2)
        with open("datasave.json", "w") as fy:  # Write
            fy.write(string)

    if key == ord('r'):
        parts = {'p1': '-', 'p2': '-', 'p3': '-'}
