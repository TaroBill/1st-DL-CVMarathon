import cv2
p1=(60,40)
p2=(420,510)
img = cv2.imread("C://pictures//lena.png")
# 原始 BGR 圖片轉 HSV 圖片
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 對明亮度做直方圖均衡 -> 對 HSV 的 V 做直方圖均衡
img[..., -1] = cv2.equalizeHist(img[..., -1])
# 將圖片轉回 BGR
img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

cv2.rectangle(img,p1,p2,(0,0,255),3)#-1是填滿

img = img[:,::-1,:]
pp1 = (int(img.shape[1]-p1[0]),p1[1])
pp2 = (int(img.shape[1]-p2[0]),p2[1])
ScaleX = 0.5
ScaleY = 0.5
imgscale = cv2.resize(img,None,fx=ScaleX,fy=ScaleY,interpolation=cv2.INTER_AREA)

pp1 = tuple(int(x*ScaleX) for x in pp1)
pp2 = tuple(int(x*ScaleX) for x in pp2)

print(pp1,pp2)
cv2.imshow("small",imgscale)
k = cv2.waitKey(0)
cv2.destroyAllWindows()

