# Import the necessary packages
from __future__ import print_function
import cv2

# Load the image and show it
image = cv2.imread("RGB.JPG")
cv2.imshow("Original", image)

print("NumPy array: {}".format(image.shape))

# Images are just NumPy arrays. The top-left pixel can be
# found at (10, 10)
(b, g, r) = image[10, 10]
print("Pixel at (10, 10) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
(b, g, r) = image[10, 420]
print("Pixel at (10, 420) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
(b, g, r) = image[170, 10]
print("Pixel at (170, 10) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
(b, g, r) = image[170, 420]
print("Pixel at (170, 420) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


cv2.waitKey(0)
