import cv2 as cv

img = cv.imread('./data/1.png')
cv.imshow('read_img', img)
cv.waitKey(1000)
# 传入0无限等待，单位毫秒
cv.destroyAllWindows()
# 释放内存 底层c++
