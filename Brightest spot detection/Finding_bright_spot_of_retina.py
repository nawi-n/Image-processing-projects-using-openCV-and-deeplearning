import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image file")
ap.add_argument("-r", "--radius", type=int, help="radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

# Load the image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# Make a copy of the original image
orig = image.copy()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)
cv2.waitKey(0)

# Apply Gaussian blur to the grayscale image
if args["radius"]:
    gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)

# Find the location of the maximum intensity in the blurred image
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

# Draw a circle around the maximum intensity location
image = orig.copy()
cv2.circle(image, maxLoc, args["radius"], (255, 0, 0), 2)

# Display the output image with the circle drawn
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
