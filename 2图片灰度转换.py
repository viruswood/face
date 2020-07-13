import cv2 as cv

img = cv.imread('./data/1.jpg')
cv.imshow('BGR_img', img)
# 将img 图片进行灰度转换
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite('data/gray_sss.jpg', gray_img)
cv.imshow('gray_img', gray_img)
cv.waitKey(0)
cv.destroyAllWindows()
