import cv2

image= cv2.imread("jeep.png")
(h,w,d)=image.shape

center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,-45,1.0)
rotated=cv2.wrapAffine(image, M, (w,h))
cv2.imshow("OpenCV Rotation",rotated)
cv2.waitKey(0)
