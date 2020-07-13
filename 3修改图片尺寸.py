import cv2 as cv

img = cv.imread('data/1.jpg')
cv.imshow('old_img', img)
print('修改前图片的形状', img.shape)
resize_img = cv.resize(img, dsize=(200, 240))
print('修改后图片的形状', resize_img.shape)
cv.imshow('img', resize_img)
while True:
    if ord('q') == cv.waitKey(0):
        # 获取键盘输入asii码值
        break
cv.destroyAllWindows()
