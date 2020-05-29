import cv2
import numpy as np
import time

carClassifier = cv2.CascadeClassifier("./Haarcascades/haarcascade_car.xml")

cap = cv2.VideoCapture("./cars.avi")

while cap.isOpened():
    time.sleep(0.10)
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cars = carClassifier.detectMultiScale(gray,1.2,2)
        
    for (x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)
        
    cv2.imshow("Car Detection", frame)
    
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cv2.destroyAllWindows()
