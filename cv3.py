import cv2
import numpy as np
img = cv2.imread("C://pictures//lena.png")
#直方圖均衡
# =============================================================================
# imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgG_equal = cv2.equalizeHist(imgGRAY)
# img_gray_equalHist = np.hstack((imgGRAY, imgG_equal))
# cv2.imshow('GrayEQ',img_gray_equalHist)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

#調整飽和度
# =============================================================================
# percentOfChange=-0.2
# imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# imgHSV = imgHSV.astype('float32')
# imgHSV[...,-1] = imgHSV[...,-1]/255+percentOfChange
# imgHSV[imgHSV[..., -1] > 1] = 1
# imgHSV[...,-1]*=255
# imgHSV = imgHSV.astype('uint8')
# imgHSV = cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR)
# imgChange = np.hstack((img, imgHSV))
# cv2.imshow('30%上升下降飽和度',imgChange)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

#對比/明亮調整 Alpha對比度(1~3) Beta明亮度(0~100)
Alpha = 1
Beta = 70
imgLight = cv2.convertScaleAbs(img,alpha=Alpha,beta=Beta)
Alpha = 1.5
Beta = 0
imgContrast = cv2.convertScaleAbs(img,alpha=Alpha,beta=Beta)
img_L_C = np.hstack((img,imgLight,imgContrast))
cv2.imshow('P1_Normal_P2_Light_P3_Contrast',img_L_C)
cv2.waitKey(0)
cv2.destroyAllWindows()


