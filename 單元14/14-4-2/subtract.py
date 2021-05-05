# Import the necessary packages
import cv2
import numpy as np

# Load the image and show some basic information on it
frame1 = cv2.imread("frame1.jpg")
frame2 = cv2.imread("frame2.jpg")
print(frame1.shape)
print(frame2.shape)
imageSub = cv2.subtract(frame1,frame2)

# Show the image and wait for a keypress
cv2.imshow("frame1", frame1)
cv2.imshow("frame2", frame2)
cv2.imshow("OpenCV Subtract", imageSub)

cv2.waitKey(0)


