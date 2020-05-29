import cv2
import numpy as np

faceClassifier = cv2.CascadeClassifier("./Haarcascades/haarcascade_frontalface_default.xml")
eyeClassifier = cv2.CascadeClassifier("./Haarcascades/haarcascade_eye.xml")

def detect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces = faceClassifier.detectMultiScale(gray,1.3,3)
    
    if faces is ():
        cv2.putText(image, "No Face Detected", (150,400), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        
    for (x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0),3)
        face = gray[y:y+h, x:x+w]
        eyes = eyeClassifier.detectMultiScale(face, 1.3, 10)
        if eyes is ():
            cv2.putText(image, "No Eyes Detected", (150,350), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
        elif len(eyes) == 1:
            cv2.putText(image, "One Eye Detected", (150,350), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
        
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(image, (x+ex,y+ey), (x+ex+ew, y+ey+eh), (127,0,0), 3)
    
    return image

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Face and Eye Detect", detect(frame))
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cv2.destroyAllWindows()
