import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import copy

# img read
img = cv.imread('bear.jpg')

# create blank for mask
blank = np.zeros(img.shape[:2], dtype= 'uint8')

# convert gray to find easier color filter
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# use histogram to find pixel distribution in scale of gray
hist = cv.calcHist([gray], [0], mask ,[256],[0,256] ) 

plt.plot(hist)
plt.xlim([0,256])
plt.show()


# select area that we want to color
circle = cv.circle(blank, (-5+img.shape[1]//2, -60+img.shape[0]//2),160, 255, thickness = cv.FILLED)
mask = cv.bitwise_and(gray, gray, mask = circle)

# create threshold in mask to get the area we want to change
threshold, thresh = cv.threshold(mask,120, 255, cv.THRESH_BINARY)

# copy image to keep original
img_masked = copy.deepcopy(img)

# change thresh area with 255(color we want to change, in this case white)
print(threshold)

img_masked[thresh >0] = 255

cv.imshow('img',img_masked)

cv.waitKey(1)