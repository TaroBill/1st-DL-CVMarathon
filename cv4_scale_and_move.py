import cv2
import numpy as np
img = cv2.imread("C://pictures//lena.png")
# ===========翻轉+縮放==========================================================
#img1 = img[:,::-1,:]
#imghf1 = np.hstack((img,img1))
# imghf2 = imghf1[::-1,:,:]
# imgvfout = np.vstack((imghf1,imghf2))
# cv2.imshow('flip image', imgvfout)
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()
# ScaleX = 0.5
# ScaleY = 0.5
# imgscale = cv2.resize(imgvfout,None,fx=ScaleX,fy=ScaleY,interpolation=cv2.INTER_AREA)
# cv2.imshow('Scale image', imgscale)
# k = cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================
# x 平移 100 pixel; y 平移 50 pixel
M = np.array([[1, 0, 100],
              [0, 1, 50]],
              dtype=np.float32)
shift_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
img2P = np.hstack((img,shift_img))
cv2.imshow("shift",img2P)
k = cv2.waitKey(0)
cv2.destroyAllWindows()