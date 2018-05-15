import numpy as np
import random
import cv2

def noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 256
            else:
                output[i][j] = image[i][j]
    return output

image = cv2.imread('melonfilter.jpg',0) # Only for grayscale image
noise_img = noise(image,0.1)
cv2.imwrite('noise.jpg', noise_img)
cv2.imshow('image1' , image)
cv2.imshow('image2' , noise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

