import cv2
image=cv2.imread("jeep.png")
output=image.copy()
cv2.rectangle(output,(450,80),(550,180),(0,0,255),2)
cv2.imshow("rectangle",output)
cv2.waitKey(0)
