import numpy as np
import os
import cv2

def noisy(gauss,image):
      row,col,ch= image.shape
      mean = 0
      var = 0.1
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + gauss
      return noisy

image = cv2.imread('noise.jpg',0)
noise_img = noisy(image,0.05)
cv2.imwrite('noisy.jpg', noise_img)
cv2.imshow('image' , image)
cv2.imshow('image' , noise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

