import cv2
i=0
img = [cv2.imread("C:\\pictures/lena.png")]
img.append(cv2.cvtColor(img[0],cv2.COLOR_BGR2HSV))
img.append(cv2.cvtColor(img[0],cv2.COLOR_BGR2HLS))
img.append(cv2.cvtColor(img[0],cv2.COLOR_BGR2LAB))
Color=["RGB","HSV","HLS","LAB"]
while(True):
    cv2.imshow(Color[i],img[i])
    k = cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        break
    i= 0 if i>=3 else i+1