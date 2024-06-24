import cv2

image=cv2.imread("jeep.png")
resized= cv2.resize(image,(200,200))
cv2.imshow("Fixed Resizing",resized)
cv2.waitKey(0)
