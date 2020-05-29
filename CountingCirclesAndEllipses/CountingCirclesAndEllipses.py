import cv2
import numpy as np

image = cv2.imread("./blobs.jpg", 0)

##PART 1: DETECT NUMBER OF BLOBS
# Intialize the detector using the default parameters NOTE: USE _create !!!!!!
detector = cv2.SimpleBlobDetector_create()
 
# Detect blobs
keypoints = detector.detect(image)
 
# Draw blobs on our image as green circles
blank = np.zeros((1,1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

cv2.putText(blobs, "Total Number of Blobs = " + str(len(keypoints)), 
            (20,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,0,255), 2)



cv2.imshow("Blobs", blobs)

cv2.waitKey()


##PART 2: DETECT NUMBER OF CIRCLES
#Differentiate between circles and ellipses
params = cv2.SimpleBlobDetector_Params()

#Set Params
params.filterByInertia = True
params.minInertiaRatio = 0.5


#Set up Detector with Params
detectorDiff = cv2.SimpleBlobDetector_create(params)
keypointsDiff = detectorDiff.detect(image)

blankDiff = np.zeros((1,1)) 
blobsDiff = cv2.drawKeypoints(image, keypointsDiff, blankDiff, (0,255,0), cv2.DRAW_MATCHES_FLAGS_DEFAULT)

cv2.putText(blobsDiff, "Total Number of Circles = " + str(len(keypointsDiff)), 
            (20,550), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,0,255), 2)

cv2.imshow("Circles", blobsDiff)

cv2.waitKey()
cv2.destroyAllWindows()
