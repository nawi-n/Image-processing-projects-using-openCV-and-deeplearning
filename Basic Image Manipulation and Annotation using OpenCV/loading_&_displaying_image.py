import cv2

image= cv2.imread("jeep.png")
(h,w,d)=image.shape
print("width=(),height=(),depth=()".format(w,h,d))

cv2.imshow("image",image)
cv2.waitKey(0)
