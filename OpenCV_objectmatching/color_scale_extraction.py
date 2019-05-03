import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def get_object(input):

    BLACK_THRESHOLD = 200
    LOW_SIZE_THRESHOLD = 30
    MAX_SIZE_THRESHOLD = 450
    # Denoising
    imgray = cv2.GaussianBlur(input, (5, 5), 0)
    # imgray = cv2.cvtColor(imgray, cv2.COLOR_BGR2GRAY)

    # Trying different Thresholding techniques
    # ret, thresh = cv2.threshold(imgray,10,200,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret, thresh = cv2.threshold(imgray,0,255,cv2.THRESH_TRIANGLE)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.imshow('thresh', thresh)

    idx = 0
    for cnt in contours:
        idx += 1
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img[y:y + h, x:x + w]
        if h < LOW_SIZE_THRESHOLD or w < LOW_SIZE_THRESHOLD or\
                h > MAX_SIZE_THRESHOLD or w > MAX_SIZE_THRESHOLD:
            continue
        # cv2.imwrite(str(idx) + '.png', roi)
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 0, 0), 2)

    return img



# Open an image using Opencv
img = cv2.imread("image_tech/Q2.jpeg")

# Convert the image into different colorspaces
# cvt_image = cv2.cvtColor(img,cv2.COLOR_BGR2HSV_FULL)
cvt_image = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
# cvt_image = cv2.cvtColor(img,cv2.COLOR_BGR2LUV)
# Save each channel of the image seperately
c1 = cvt_image[:, :, 0]
c2 = cvt_image[:, :, 1]
c3 = cvt_image[:, :, 2]

# Create a new window to show all the three channels seperately
f, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(10,5))
ax1.set_title("Channel 1")
ax1.imshow(c1)
ax2.set_title("Channel 2")
ax2.imshow(c2)
ax3.set_title("Channel 3")
ax3.imshow(c3)
plt.show()
im= c1
print(im.shape)
im = cv2.resize(im, (640, 480))

out = get_object(im)

cv2.imshow('Threshold', img)
cv2.imshow('Output', out)
cv2.waitKey()