import cv2

image = cv2.imread("jeep.jpg")
output = image.copy()

cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)

cv2.imshow("Line", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
