import cv2

image = cv2.imread("jeep.png")
(B,G,R)=image[100,50]
print("R={},G={},B={}".format(R,G,B))
