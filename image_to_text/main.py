import time
import cv2


def putTextRect(img, text, pos, font, scale, colorT=(255, 255, 255), thickness=3,
                colorR=(0, 0, 0), offset=1):
    ox, oy = pos
    (w, h), _ = cv2.getTextSize(text, font, scale, thickness)
    x1, y1, x2, y2 = ox - offset, oy + offset, ox + w + offset, oy - h - offset
    cv2.rectangle(img, (x1, y1), (x2, y2), colorR, cv2.FILLED)
    cv2.putText(img, text, (ox, oy), font, scale, colorT, thickness, -1)

    return img, [x1, y2, x2, y1]


def capture(data):
    import cv2
    cap = cv2.VideoCapture(0)

    while True:
        data['cap'] = cap.read()


def main(data):
    import cv2
    import pytesseract
    from datetime import datetime
    from read_barcode import read_barcodes
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    t1 = datetime.now()
    while True:
        t2 = t1
        t1 = datetime.now()
        data['fps'] = round(1 / max(0.001, (t1 - t2).total_seconds()), 1)
        s, img = data['cap']
        if s:
            texts = pytesseract.image_to_string(
                img,
                config='--psm 6 -c tessedit_char_whitelist=0123456789[]:ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            )
            for text in texts.split('\n'):
                if text == '':
                    continue
                # print("--->", text)
                if 'MC' in text:
                    data['MC'] = text
                if 'QTY' in text:
                    data['QTY'] = text
                if 'LN' in text:
                    ndmy = text.strip().strip('LN').strip().strip(':').strip()
                    if len(ndmy) == 7:
                        l = ndmy[0:2]
                        d = ndmy[2:4]
                        m = ndmy[4]
                        y = ndmy[5:]
                        print((l, d, m, y,))
                        if all(i.isdigit() for i in (l, d, y)) and m in 'ABCDEFGHIJKL':
                            d = int(d)
                            y = int(y) + 2000
                            m = ord(m) - ord('A') + 1
                            if 1 <= d <= 31:
                                data['LN'] = text
                                data['date'] = datetime(year=y, month=m, day=d)
                                data['lot'] = int(l)

                                data['data complete'] = True, data['data complete'][1]

            bar = read_barcodes(img)
            if bar:
                data['barcode'] = bar
                if len(bar) == 20 and '92' in bar and '30' in bar:
                    MC, QTY = bar.split('30')
                    MC = bar.split(QTY)[0]

                    data['bar QTY'] = QTY
                    data['bar MC'] = MC

                    data['data complete'] = data['data complete'][0], True


def getkey(data):
    import pyperclip
    import keyboard

    while True:
        event = keyboard.read_event()
        stamp_time = event.time
        event_type = event.event_type
        name = event.name
        if event_type == 'up' and name == 'right ctrl':
            if all(data['data complete']):
                pyperclip.copy(data['bar MC'])
                keyboard.press_and_release('Ctrl + v, \n')
                time.sleep(0.1)
                pyperclip.copy(data['bar QTY'])
                time.sleep(0.1)
                keyboard.press_and_release('Ctrl + v, \n')
                time.sleep(0.1)
                pyperclip.copy(data['LN'])
                time.sleep(0.1)
                keyboard.press_and_release('Ctrl + v, \n')
                time.sleep(0.1)
                pyperclip.copy(str(data['lot']))
                time.sleep(0.1)
                keyboard.press_and_release('Ctrl + v, \n')
                time.sleep(0.1)
                pyperclip.copy(str(data['date']))
                time.sleep(0.1)
                keyboard.press_and_release('Ctrl + v, \n')

                data['data complete'] = False, False

                data['MC'] = ''
                data['LN'] = ''
                data['QTY'] = ''

                data['barcode'] = ''
                data['bar MC'] = ''
                data['bar QTY'] = ''

                data['date'] = ''
                data['lot'] = ''


def show(data):
    import cv2

    while True:
        s, img = data['cap']
        if s:
            cv2.line(img, (0, 100), (1000, 100), (255, 0, 0), 1)
            cv2.line(img, (0, 200), (1000, 200), (255, 0, 0), 1)
            cv2.line(img, (0, 300), (1000, 300), (255, 0, 0), 1)
            cv2.line(img, (0, 400), (1000, 400), (255, 0, 0), 1)
            putTextRect(img, f"fps: {data['fps']}",
                        (10, 20 + 20 * 0), 1, 1, (255, 255, 0), 1)
            putTextRect(img, f"data {data['data complete']}",
                        (10, 20 + 20 * 1), 1, 1, (0, 0, 255), 1)
            if all(data['data complete']):
                putTextRect(img, f"data {data['data complete']}",
                            (10, 20 + 20 * 1), 1, 1, (0, 255, 0), 1)

            putTextRect(img, data['MC'],
                        (10, 70 + 20 * 0), 1, 1, (0, 255, 0), 1)
            putTextRect(img, data['QTY'],
                        (10, 70 + 20 * 1), 1, 1, (0, 255, 0), 1)
            putTextRect(img, data['LN'],
                        (10, 70 + 20 * 2), 1, 1, (0, 255, 0), 1)
            putTextRect(img, f"{data['date']}",
                        (10, 70 + 20 * 4), 1, 1, (0, 255, 0), 1)
            putTextRect(img, f"{data['lot']}",
                        (10, 70 + 20 * 5), 1, 1, (0, 255, 0), 1)
            putTextRect(img, data['barcode'],
                        (10, 70 + 20 * 7), 1, 1, (0, 255, 0), 1)
            putTextRect(img, data['bar MC'],
                        (10, 70 + 20 * 8), 1, 1, (0, 255, 0), 1)
            putTextRect(img, data['bar QTY'],
                        (10, 70 + 20 * 9), 1, 1, (0, 255, 0), 1)

            cv2.imshow('frame', img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break


if __name__ == '__main__':
    import multiprocessing

    manager = multiprocessing.Manager()
    data = manager.dict()
    data['cap'] = (None, None)
    data['fps'] = 0
    data['data complete'] = False, False

    data['MC'] = ''
    data['LN'] = ''
    data['QTY'] = ''

    data['barcode'] = ''
    data['bar MC'] = ''
    data['bar QTY'] = ''

    data['date'] = ''
    data['lot'] = ''

    capture_process = multiprocessing.Process(target=capture, args=(data,))
    main_process = multiprocessing.Process(target=main, args=(data,))
    show_process = multiprocessing.Process(target=show, args=(data,))
    getkey_process = multiprocessing.Process(target=getkey, args=(data,))

    capture_process.start()
    main_process.start()
    show_process.start()
    getkey_process.start()

    capture_process.join()
    main_process.join()
    show_process.join()
    getkey_process.join()
