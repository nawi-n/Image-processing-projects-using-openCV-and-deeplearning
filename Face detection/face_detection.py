#arguments

import numpy as np
import argparse
import cv2

ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
ap.add_argument("-p","--prototxt",required=True,help="path to caffe 'deploy' prototxt file")
ap.add_argument("-m","--model",required=True,help="path to caffe pre-trained model")
ap.add_argument("-c","--confidence",type=float,default=0.2,help=
                "minimum probability to filter weak detections")
args=vars(ap.parse_args())

#blobfromimage

print("[INFO] loading model...")
net=cv2.dnn.readNetFromCaffe(args["prototxt"],args["model"])

image=cv2.imread(args["image"])
(h,w)=image.shape[:2]
blob=cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),0.007834,(300,300),127.5)

print("[INFO] computing object detections...")

#object detections

net.setInput(blob)
detections=net.forward()

#final output

for i in np.arange(0, detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > args["confidence"]:
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        text = "{:.2f}%".format(confidence * 100)
        y = startY - 10 if startY - 10 > 10 else startY + 10
        cv2.rectangle(image, (startX, startY), (endX, endY), (0,0,255), 2)
        
        cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45,(0,0,255), 2)

cv2.imshow("output", image)
cv2.waitKey(0)




