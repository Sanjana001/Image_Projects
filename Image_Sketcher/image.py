import cv2
import numpy as np
import os
#read the image
img = cv2.imread(r"bird.jpg")
img1 = cv2.imread(r"effect.jpg")
directory = r"C:\Users\HP\Desktop"
#resize the images
img = cv2.resize(img,(1000,800))
img1 = cv2.resize(img1,(1000,800))
#blur the image
color = cv2.GaussianBlur(img,(3,3),5)
#convert the color of image into gray
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
edges = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 8)
image = cv2.bitwise_and(color,color,mask=edges)
img = cv2.addWeighted(image,0.9,img1,0.2,0)
#to change the directory
os.chdir(directory)
#save the image with any name
cv2.imwrite("Image.jpg",img)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()