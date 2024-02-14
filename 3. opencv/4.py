import cv2

img = cv2.imread('img.png')
print(img.shape)

cv2.rectangle(img, [100, 200], [300, 400], (0, 255, 0))
cv2.circle(img, [500, 500], 100, (255, 0, 0))
cv2.circle(img, [500, 150], 100, (0, 0, 255), 5)
# cv2.putText(img, 'text', [200, 700], 1, 5, (255, 255, 255), 3)
cv2.imshow('img2', img)
cv2.waitKey(0)
