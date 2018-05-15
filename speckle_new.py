import cv

im = cv.LoadImage('melon.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
mult_noise = cv.CreateImage((im.width,im.height), cv.IPL_DEPTH_32F, 1)

cv.RandArr(cv.RNG(6), mult_noise, cv.CV_RAND_NORMAL, 1, 0.1)    

cv.Mul(im, mult_noise, im)

cv.ShowImage("tree with speckle noise", im)
cv.WaitKey(0)
