import cv2
from numpy import *
a = array( [2,3,4] )
b = array( [ (1.5,2,3), (4,5,6) ] )

print a
print b
image = cv2.imread('0.png')
cv2.namedWindow("img")
cv2.imshow("img",image)
cv2.waitKey (0) 