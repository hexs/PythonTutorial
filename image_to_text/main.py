import time


def capture(data):
    import cv2
    cap = cv2.VideoCapture(0)

    while True:
        data['cap'] = cap.read()


def main(data):
    import cv2
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    while True:
        s, img = data['cap']
        if s:
            text = pytesseract.image_to_string(
                img,
                config='--psm 6 -c tessedit_char_whitelist=0123456789[]:ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            )
            for i in text.split('\n'):
                if i == '':
                    continue
                print("--->", i)
                if 'MC' in i:
                    data['MC'] = i
                if 'LN' in i:
                    data['LN'] = i
                if 'QTY' in i:
                    data['QTY'] = i

            cv2.line(img, (0, 100), (1000, 100), (255, 0, 0), 1)
            cv2.line(img, (0, 200), (1000, 200), (255, 0, 0), 1)
            cv2.line(img, (0, 300), (1000, 300), (255, 0, 0), 1)
            cv2.line(img, (0, 400), (1000, 400), (255, 0, 0), 1)

            cv2.putText(img, data['MC'], (50, 50 - 20), 1, 1, (0, 255, 0), 1)
            cv2.putText(img, data['QTY'], (50, 50), 1, 1, (0, 255, 0), 1)
            cv2.putText(img, data['LN'], (50, 50 + 20), 1, 1, (0, 255, 0), 1)

            cv2.imshow('frame', img)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break


def getkey(data):
    import pyperclip
    import keyboard

    while True:
        event = keyboard.read_event()
        stamp_time = event.time
        event_type = event.event_type
        name = event.name
        if event_type == 'up' and name == 'right ctrl':
            pyperclip.copy(data['MC'])
            keyboard.press_and_release('Ctrl + v, \n')
            time.sleep(0.1)
            pyperclip.copy(data['LN'])
            keyboard.press_and_release('Ctrl + v, \n')
            time.sleep(0.1)
            pyperclip.copy(data['QTY'])
            keyboard.press_and_release('Ctrl + v, \n')
            data['MC'] = ''
            data['LN'] = ''
            data['QTY'] = ''


if __name__ == '__main__':
    import multiprocessing

    manager = multiprocessing.Manager()
    data = manager.dict()
    data['cap'] = (None, None)
    data['MC'] = ''
    data['LN'] = ''
    data['QTY'] = ''
    capture_process = multiprocessing.Process(target=capture, args=(data,))
    show_process = multiprocessing.Process(target=main, args=(data,))
    getkey_process = multiprocessing.Process(target=getkey, args=(data,))

    capture_process.start()
    show_process.start()
    getkey_process.start()

    capture_process.join()
    show_process.join()
    getkey_process.join()
