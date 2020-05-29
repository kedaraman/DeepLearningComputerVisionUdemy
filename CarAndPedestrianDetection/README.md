# Car and Pedestrian Detection From Video

The goal of this project is to create a script that uses OpenCV to detect images, in this case cars or pedestrians. There are two Python scripts- one to detect cars in a video and another to detect pedestrians in a video. Both of these projects use the HAAR Cascade Classifiers, specifically the car and fullbody classifiers. These classifiers are included in the Haarcascades folder.

As can be seen in the picture below, the Car detection script parses through a video, and detects all cars. The parameters used in detectMultiScale() for the HAAR Cascade Classification were tuned for this purpose.

![Demo of Car Detection](https://github.com/kedaraman/DeepLearningComputerVisionUdemy/blob/master/CarAndPedestrianDetection/CarDemo.PNG)

As can be seen in the picture below, the Pedestrian detection script also parses through a similar video, detecting all pedestrians. This is done using the fullbody HAAR classifier. The parameters of this classifier were also tuned for this use case.

![Demo of Pedestrian Detection](https://github.com/kedaraman/DeepLearningComputerVisionUdemy/blob/master/CarAndPedestrianDetection/PedestrianDemo.PNG)
