![Shapes to Identify](https://github.com/kedaraman/DeepLearningComputerVisionUdemy/blob/master/IdentifyShapes/someshapes.jpg)

Above is the image that we want to classify shapes from. There are 5 shapes: Rectangle, Square, Triangle, Circle, and Star.

Using the Contour Approximation Image Segmentation technique, we find the contours for each image in the picture using the OpenCV findContours function. We then approximate the contours as a polygon using the approxPolyDP function, and classify the shapes based on the number of sides that it has.

Below is the final result of classifying the shapes.

![Demo of Shape Identification](https://github.com/kedaraman/DeepLearningComputerVisionUdemy/blob/master/IdentifyShapes/Demo.PNG)
