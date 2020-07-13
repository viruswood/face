import cv2 as cv

img = cv.imread('data/1.jpg')
x, y, w, h = 100, 100, 100, 100
# cv.rectangle(img, (x, y, x + w, y + h), color=(0, 255, 0), thickness=2)
cv.circle(img, center=(x + w // 2, y + h // 2), radius=w // 2, color=(0, 255, 255))
cv.imshow('img_aaa', img)
while True:
    if ord('q') == cv.waitKey(0):
        break
cv.destroyAllWindows()
