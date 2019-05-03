import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_object(input):

    BLACK_THRESHOLD = 200
    LOW_SIZE_THRESHOLD = 30
    MAX_SIZE_THRESHOLD = 450

    imgray = cv2.GaussianBlur(input, (5, 5), 0)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(imgray,0,255,cv2.THRESH_TRIANGLE)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #cv2.imshow('thresh', thresh)

    idx = 0
    for numbers,cnt in enumerate(contours):
        idx += 1
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img[y:y + h, x:x + w]
        if h < LOW_SIZE_THRESHOLD or w < LOW_SIZE_THRESHOLD or\
                h > MAX_SIZE_THRESHOLD or w > MAX_SIZE_THRESHOLD:
            continue
        cv2.imwrite(str(numbers) + '.png', roi)

        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 0, 0), 2)

    return img

def remove_bg(input,background):
    subtracted = np.abs(input - background)
    subtracted[subtracted < 0 ] = 0
    subtracted[subtracted > 240] = 0
    print(subtracted)
    return subtracted

if __name__ == "__main__":


    img = cv2.imread('image_tech/T1.jpeg')
    #img = cv2.imread('image_tech/T7.jpeg')
    img = cv2.resize(img,(640,480))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)


    bg_img = cv2.imread('image_tech/Q1.jpeg')
    bg_img = cv2.resize(bg_img, (640, 480))
    bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)


    #abc = remove_bg(img,bg_img)
    out = get_object(img)

    cv2.imshow('Threshold', img)
    cv2.imshow('Output', out)
    cv2.waitKey()
