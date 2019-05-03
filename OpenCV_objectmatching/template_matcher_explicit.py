import numpy as np
import matplotlib.pyplot as plt

import cv2

MIN_MATCH_COUNT = 10
# img1 = cv2.imread('/home/deepan/PycharmProjects/techchallenge/ContestImages/Targets/Target0.jpg',0)          # queryImage
# img2 = cv2.imread('/home/deepan/PycharmProjects/techchallenge/ContestImages/Queries/Target0/Img16.jpg',0)    # trainImage

img1= cv2.imread('/home/deepan/PycharmProjects/techchallenge/OpenCV_objectmatching/image_tech/Q3.jpeg',0)          # queryImage
img2= cv2.imread('/home/deepan/PycharmProjects/techchallenge/OpenCV_objectmatching/image_tech/T3a.jpeg', 0)         # trainImage
img1 = cv2.GaussianBlur(img1,(5,5),0)
img2 = cv2.GaussianBlur(img2,(5,5),0)
cv2.imshow('Template',img1)
cv2.waitKey()
cv2.imshow('Input',img2)
cv2.waitKey()


w, h = template.shape[::-1]
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # Apply template Matching
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()