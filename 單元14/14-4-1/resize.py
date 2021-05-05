#!/usr/bin/env python
# -*- coding: utf8 -*-
import cv2
import numpy as np

img = cv2.imread('baby.jpg')
rows,cols, channel = img.shape

dst = cv2.resize(img,(2*cols,rows),interpolation = cv2.INTER_CUBIC)
dst1 = cv2.resize(img,(cols,2*rows),interpolation = cv2.INTER_LINEAR)
dst2 = cv2.resize(img,(int(cols/2),int(rows/2)),interpolation = cv2.INTER_AREA)


cv2.imshow('original',img)
cv2.imshow('CUBIC wide magnification 3',dst)
cv2.imshow('LINEAR high magnification 2',dst1)
cv2.imshow('AREA narrow 1/2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()

