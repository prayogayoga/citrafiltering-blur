import numpy as np
import cv2

img = cv2.imread("melonnoise.jpg")

cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unfiltered Image',img)
cv2.waitKey(0)
print "Processing..."

myIMG = cv2.medianBlur(img, (3,3))

cv2.imwrite('noiseee.jpg', myIMG)
cv2.namedWindow('Processed Image', cv2.WINDOW_NORMAL)
cv2.imshow('Processed Image', myIMG)
cv2.waitKey(0)
print "Done!"
