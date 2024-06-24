import cv2

# Load the image
image = cv2.imread("Jeep.png")

# Create a copy of the image
output = image.copy()

# Draw a circle on the output image
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)  # (300, 150) is the center, 20 is the radius, (255, 0, 0) is blue color, -1 is filled circle

# Display the image with the circle
cv2.imshow("Circle", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
