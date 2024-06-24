import argparse
import imutils
import cv2

# Parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

# Read the image
image = cv2.imread(args["image"])

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform edge detection
edged = cv2.Canny(gray, 30, 150)

# Threshold the image
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]

# Find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Make a copy of the original image
output = image.copy()

# Draw contours on the original image
for c in cnts:
    cv2.drawContours(output, [c], -1, (240, 0, 159), 3)

# Count the number of contours
num_contours = len(cnts)
text = f"I found {num_contours} objects!"

# Add text to the output image
cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (240, 0, 159), 2)

# Display the output image with contours and count
cv2.imshow("Contours", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
