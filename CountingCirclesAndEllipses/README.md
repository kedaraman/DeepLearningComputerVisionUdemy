# Differentiating Ellipses and Circles
![Shapes to ID](https://github.com/kedaraman/DeepLearningComputerVisionUdemy/blob/master/CountingCirclesAndEllipses/blobs.jpg)

Above is the image that contains both circles and ellipses. We want to differentiate between the two.

Using the OpenCV SimpleBlobDetector, we differentiate between a circle and an ellipse using the Inertia filter, marking an updated image. We first detect all blobs (left image on bottom) and then detect just the circles (right image on bottom)

![Demo of Circle and Ellipse Counting](https://github.com/kedaraman/DeepLearningComputerVisionUdemy/blob/master/CountingCirclesAndEllipses/Demo.PNG)
