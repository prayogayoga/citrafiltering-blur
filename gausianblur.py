import numpy as np
import cv2

# Definition of functions

def loopForBlurring(sizeOfKernel, howManyTimes, givenIMG, sigmax):
    for x in range(howManyTimes):
        givenIMG = cv2.GaussianBlur(givenIMG, sizeOfKernel, sigmax)
    return givenIMG

# Main part

img = cv2.imread("melonfilter.jpg")

cv2.namedWindow('Unfiltered Image', cv2.WINDOW_NORMAL)
cv2.imshow('Unfiltered Image',img)
cv2.waitKey(0)
print "Processing..."

processedImage = loopForBlurring((29,29), 1, img, 0) # Gaussian blur
head = img[720:1200, 880:1300] # Cut the parrot head from the original image
processedImage[720:1200, 880:1300] = head # Paste the parrot head to the processed image


cv2.imwrite('noisee.jpg', processedImage)
cv2.namedWindow('Filtered one time, kernel size 29', cv2.WINDOW_NORMAL)
cv2.imshow('Filtered one time, kernel size 29', processedImage)
print "Done!"
cv2.waitKey(0)
