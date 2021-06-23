import cv2 as cv
from matplotlib import pyplot as plt
# print(cv.__version__)
#this is were I started coding. First thing I am going to do -> Read an image: 

img = cv.imread('./images/1.png',0) #0 means B/W
img2 = cv.imread('./images/2.png',0)

sum = img + img2
cv.imshow("sum", sum)

print("IMAGE MATRIX", img)
# Channel 0 is red
# Channel 1 is green
# Channel 2 is blue
cv.imshow("img.png", img[:,:]) #open image in another window -> if you want only 1 channel add a third index 
cropped = cv.imshow("img.png", img[0:450, 0:800]) #crops the img 
cv.waitKey(0)

print(img.shape) #returns 3 values -> H, W and DEPTH (R G B) 
print(type(img)) #img type is numpy.ndarray
print(img[50,100]) #return the value of the specific location 
#IF THE IMAGE WAS W COLOR -> img[50,100,2] USE THIRD INDEX TO CHOOSE CHANNEL

#CREATES HISTOGRAM FOR BW
plt.hist(img.ravel(),256,[0,256]); 
plt.show() #opens a window with histogram in it


#CREATES HISTORGRAM FOR COLOR 
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    #calcHist(image, channel, mask, histogram size, range)
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

