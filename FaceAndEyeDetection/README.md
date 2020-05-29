# Face and Eye Detection from Webcam

The goal of this project is to detect faces and eyes coming from live video from the user's webcam. To do this, the HAAR Cascade Classifiers for eyes and faces was used (see the Haarcascades folder for the XML files). Video frames were parsed from the webcam, and first the faces are detected. Once the faces are detected, for each face, we try to detect eyes within the bounds of the face. A demo of the project can be seen below.

![Demo of Face Detection]()
