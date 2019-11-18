import cv2
img = cv2.imread("C:\\pictures/test.png",cv2.IMREAD_GRAYSCALE)
imgRGB = cv2.imread("C:\\pictures/test.png")
cv2.imshow('rgb',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('rgb',imgRGB)
cv2.waitKey(0)
cv2.destroyAllWindows()