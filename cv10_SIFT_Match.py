import cv2
# import numpy as np

# 以灰階方式讀入圖片
img_query = cv2.imread('C://pictures//box.png', 0)
img_train = cv2.imread('C://pictures//box_in_scene.png', 0)

# img_query = cv2.resize(img_query,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# img_train = cv2.resize(img_train,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# 建立 SIFT 物件
sift = cv2.xfeatures2d_SIFT.create()

# 偵測並計算 SIFT 特徵 (keypoints 關鍵點, descriptor 128 維敘述子)
kp_query, des_query = sift.detectAndCompute(img_query, None)
kp_train, des_train = sift.detectAndCompute(img_train, None)
# 建立 Brute-Force Matching 物件
bf = cv2.BFMatcher(cv2.NORM_L2)

# 以 knn 方式暴力比對特徵
matches = bf.knnMatch(des_query, des_train, k=2)

# 透過 D.Lowe ratio test 排除不適合的配對
candidate = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        candidate.append([m])

# 顯示配對結果
img_show = cv2.drawMatchesKnn(img_query, kp_query, img_train, kp_train, candidate, None, flags=2)

# 顯示圖片
while True:
    cv2.imshow('matches', img_show)
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break