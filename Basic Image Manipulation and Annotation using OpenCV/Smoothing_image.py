import cv2

image=cv2.imread("jeep.png")
resized= cv2.resize(image,(500,500))
blurred=cv2.GaussianBlur(resized,(11,11),0)
cv2.imshow("Blurred",blurred)
cv2.waitKey(0)
