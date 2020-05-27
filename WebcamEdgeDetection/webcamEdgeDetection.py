import cv2
import numpy as np

def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
#     noise_reduced = cv2.bilateralFilter(image, 9, 75, 75)
    noise_reduced = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    edges = cv2.Canny(noise_reduced, 10, 70)
    
    invert_colors = cv2.bitwise_not(edges)
    
    return invert_colors

cap = cv2.VideoCapture(0)#Starts the webcam

while True:
    ret, frame = cap.read()
#     cv2.imshow('Original', frame)
    cv2.imshow('Webcam Edge Detection', sketch(frame))
    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

#Upon termination, release camera and close all windows
cap.release()
cv2.destroyAllWindows()
