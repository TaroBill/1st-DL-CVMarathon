import cv2 
img = cv2.imread("C://pictures//Leo1.jpg")
# 轉灰階圖片
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ScaleX = .5
ScaleY = .5
imgscale = cv2.resize(img_gray,None,fx=ScaleX,fy=ScaleY,interpolation=cv2.INTER_AREA)
img = cv2.resize(img,None,fx=ScaleX,fy=ScaleY,interpolation=cv2.INTER_AREA)
# 建立 SIFT 物件
SIFT_detector = cv2.xfeatures2d.SIFT_create()

# 取得 SIFT 關鍵點位置
keypoints = SIFT_detector.detect(imgscale, None)

img_show = cv2.drawKeypoints(imgscale, keypoints, img)
cv2.imshow('SIFT', img_show)
cv2.waitKey(0)
cv2.destroyAllWindows()