import cv2
import cvzone

BLACK = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
ENDC = '\033[0m'
BOLD = '\033[1m'
ITALICIZED = '\033[3m'
UNDERLINE = '\033[4m'


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.xy = x, y

    def __str__(self):
        return f'{BLUE}({self.x} {self.y}){ENDC}'


class Rect:
    def __init__(self, name, p1: Point, p2: Point):
        self.name = name
        self.p1 = p1
        self.p2 = p2
        self.xywh()

    def __str__(self):
        return f'Rect|{self.name} {self.p1}{self.p2}'

    def has_point_on_it(self, p: Point):
        return self.x < p.x < self.x + self.w and self.y < p.y < self.y + self.h

    def xywh(self):
        self.x = min(self.p1.x, self.p2.x)
        self.y = min(self.p1.y, self.p2.y)
        self.w = abs(self.p1.x - self.p2.x)
        self.h = abs(self.p1.y - self.p2.y)
        return self.x, self.y, self.w, self.h

    def xyxy(self):
        self.x1 = min(self.p1.x, self.p2.x)
        self.y1 = min(self.p1.y, self.p2.y)
        self.x2 = max(self.p1.x, self.p2.x)
        self.y2 = max(self.p1.y, self.p2.y)
        return self.x1, self.y1, self.x2, self.y2

    def show(self, img, pos):
        cv2.rectangle(img, list(self.p1.xy), list(self.p2.xy), (255, 0, 0), 2)
        if self.has_point_on_it(pos):
            cv2.rectangle(img, list(self.p1.xy), list(self.p2.xy), (0, 255, 0), 2)
        self.xyxy()
        cvzone.putTextRect(img, self.name, (self.x1, self.y1), 1, 1,
                           (255, 255, 0), (0, 0, 0), offset=2)


if __name__ == '__main__':
    p1 = Point(100, 200)
    p2 = Point(300, 400)
    print(p1)
    print(p2)
    r1 = Rect('name', p1, p2)
    print(r1)
