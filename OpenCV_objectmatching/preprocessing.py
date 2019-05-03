import numpy as np
import cv2
import matplotlib.pyplot as plt
f, axs = plt.subplots(2,2,figsize=(15,6))

im = cv2.imread('image_tech/T3.jpeg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

cv2.imshow("input_img", im)
cv2.waitKey()
ret, thresh = cv2.threshold(imgray, 120, 70, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im,contours,-1,(0,255,0),3)
cv2.imshow("window title", im)
cv2.waitKey()
