import numpy as np
import matplotlib.pyplot as plt

import cv2


# img1 = cv2.imread('/home/deepan/PycharmProjects/techchallenge/ContestImages/Targets/Target0.jpg',0)          # queryImage
# img2 = cv2.imread('/home/deepan/PycharmProjects/techchallenge/ContestImages/Queries/Target0/Img16.jpg',0)    # trainImage

img1i = cv2.imread('/home/deepan/PycharmProjects/techchallenge/bag_images/Nut.jpg',0)          # queryImage
img2i = cv2.imread('/home/deepan/PycharmProjects/techchallenge/bag_images/All.jpg', 0)         # trainImage
img1 = cv2.GaussianBlur(img1i,(5,5),0)
img2 = cv2.GaussianBlur(img2i,(5,5),0)
# f, axs = plt.subplots(2,2,figsize=(15,6))

# plt.subplot(131)
plt.imshow(img2i)

# plt.subplot(132)
plt.imshow(img2)



# Initiate SIFT detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
#bf=cv2.BFMatcher()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None)

plt.imshow(img3),plt.show()