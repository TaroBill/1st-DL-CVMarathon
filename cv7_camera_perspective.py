import cv2
import numpy as np
img = cv2.imread("C://pictures//lena.png")
img_perspective = img.copy()
h, w = img.shape[:2]
# 設定四對點，並取得 perspective 矩陣
point1 = np.array([[60, 40], [420, 40], [420, 510], [60, 510]], dtype=np.float32)#你要設為角落的四個點，這裡是用cv5的框框
point2 = np.array([[0, 0], [w, 0], [w, h], [0, h]], dtype=np.float32) #初始圖片最角落4個點
M = cv2.getPerspectiveTransform(point1, point2)

# perspective 轉換
img_perspective = cv2.warpPerspective(img, M, (w, h))

# 組合 + 顯示圖片
img_show = np.hstack((img, img_perspective))
cv2.imshow('perspective transform', img_show)
k = cv2.waitKey(0)
cv2.destroyAllWindows()