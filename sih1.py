#first we have to install required packeges
#pip install opencv-python -->> command to install opencv
import cv2
url = 'http://192.168.0.108:8080/video' #paste your IPv4 address
cap = cv2.VideoCapture(url)
while(True):
    ret, frame = cap.read() #read frame one by one
    if not ret or frame is None or frame.size == 0:
        break

    resized = cv2.resize(frame,(1000,700))
    cv2.imshow('frame',resized) #display resized video
    q = cv2.waitKey(1) #wait till key press
    if q == ord("q"): 
        break
cap.release() #relese capture video 
cv2.destroyAllWindows() #destroy all frame windows 