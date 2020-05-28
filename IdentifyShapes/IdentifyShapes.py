import cv2
import numpy as np

image = cv2.imread("./someshapes.jpg")

#Convert to Greyscale to process
greyImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Reduces noise/unnecessary contours
edged = cv2.Canny(greyImage,30,200)

#Find contours on the image
contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    accuracy = 0.01 * cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c, accuracy, True) #Get the polygon for the image
    cv2.drawContours(image,[approx],0,(0,255,0),2)
#     print(len(approx))
    shape = ""
    
    if len(approx) == 3:
        shape = "Triangle"
        
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(c)
        if abs(w-h) > 5:
            shape = "Rectangle"
        else:
            shape = "Square"
    elif len(approx) == 10:
        shape = "Star"
    elif len(approx) >= 15:
        shape = "Circle"
    else:
        shape = "Cant Classify"
    
    #Find Center of Mass to put text over
    M = cv2.moments(c)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.putText(image, shape, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
    cv2.imshow("Shapes to Classify", image)
    cv2.waitKey()
    




cv2.destroyAllWindows()
print("DONE")
