import cv2

image=cv2.imread("jeep.png")
roi=image[70:170,440:540]
cv2.imshow("ROI",roi)
cv2.waitKey(0)
