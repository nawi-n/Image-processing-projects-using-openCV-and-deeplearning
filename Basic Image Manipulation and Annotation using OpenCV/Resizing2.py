import cv2
image=cv2.imread("jeep.png")
(h,w,d)=image.shape

r=300.0/w
dim=(300,int(h*r))
resized=cv2.resize(image,dim)
cv2.imshow("Aspect Ratio Resize",resized)
cv2.waitKey(0)
