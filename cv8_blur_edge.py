import cv2 
import numpy as np
img = cv2.imread("C://pictures//lena.png")
#=======Blur================================
#img_blur = cv2.GaussianBlur(img,(5,5),0)
#img_blur2 = cv2.GaussianBlur(img_blur,(5,5),0)
#img_blur3 = cv2.GaussianBlur(img_blur2,(5,5),0)
#img_show = np.hstack((img_blur, img_blur2, img_blur3))
#cv2.imshow("Blur3times",img_show)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#=======sobel================================
#img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 對 x 方向做 Sobel 邊緣檢測
#img_sobel_x = cv2.Sobel(img_grey, cv2.CV_16S, dx=1, dy=0, ksize=3)
#img_sobel_x = cv2.convertScaleAbs(img_sobel_x)

# 對 y 方向做 Sobel 邊緣檢測
#img_sobel_y = cv2.Sobel(img_grey, cv2.CV_16S, dx=0, dy=1, ksize=3)
#img_sobel_y = cv2.convertScaleAbs(img_sobel_y)

# x, y 方向的邊緣檢測後的圖各以一半的全重進行合成
#img_sobel_combine = cv2.addWeighted(img_sobel_x, 0.5, img_sobel_y, 0.5, 0)
#img_show = np.hstack((img_sobel_x, img_sobel_y, img_sobel_combine))
#cv2.imshow("sobel",img_show)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#==============================================
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 對 x 方向做 Sobel 邊緣檢測
img_sobel_x = cv2.Sobel(img_grey, cv2.CV_16S, dx=1, dy=0, ksize=3)
img_sobel_x = cv2.convertScaleAbs(img_sobel_x)
img_d2 = cv2.Sobel(img_grey, cv2.CV_16S, dx=2, dy=0, ksize=3)
img_d2 = cv2.convertScaleAbs(img_d2)
img_sobel_x_unit8 = cv2.Sobel(img_grey,-1, dx=1, dy=0, ksize=3)

# x, y 方向的邊緣檢測後的圖各以一半的全重進行合成
img_show = np.hstack((img_sobel_x_unit8, img_sobel_x,img_d2 ))
cv2.imshow("unit8  dx=1  dx=2",img_show)
cv2.waitKey(0)
cv2.destroyAllWindows()