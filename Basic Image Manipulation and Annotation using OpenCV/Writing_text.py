import cv2

image = cv2.imread("jeep.png")
output = image.copy()

cv2.putText(output, "JEEP in the Jurassic Park!", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow("Text", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
