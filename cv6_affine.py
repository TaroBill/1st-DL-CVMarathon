import cv2
import numpy as np
img = cv2.imread("C://pictures//lena.png")
M_rotate = cv2.getRotationMatrix2D((img.shape[0]//2, img.shape[1]//2), 45, 0.5)
M_translate = np.array([[1, 0, 100], [0, 1, -50]], dtype=np.float32)
img = cv2.warpAffine(img, M_rotate, (img.shape[1], img.shape[0]))
img = cv2.warpAffine(img, M_translate, (img.shape[1], img.shape[0]))
cv2.imshow("Image",img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()