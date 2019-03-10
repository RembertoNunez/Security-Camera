#This is our webcam python file which allows us to track faces and bodies
#This creates a class that we use to access the camera
#The camera here will be able to dectect not only faces, but bodies as well!

import cv2 #Imports OpenCV
from imutils.object_detection import non_max_suppression #Allows us to use the function to grab bodies from stream
import numpy as np #Import numpy library
import imutils #Imports Imutils
import sys #imports system
class VideoCamera(object): #A class is defined called VideoCamera
    def __init__(self): #Self initializes a camera within a variable called video
        self.video = cv2.VideoCapture(0) #This tells to use the OpenCV function VideoCapture
    def __del__(self): 
        self.video.release() #Unlocks the object
    
    def get_frame(self): #Defines a function called get_frame takes itself as an argument
  	faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
	#Create a variable called facecascade that holds front face detection capabilities ^
	hog = cv2.HOGDescriptor() #Hog is a method that we can use to detect people
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
	#Allows us to detect people ^
        success, image = self.video.read() #Reads data from the image
	(rects, weights)= hog.detectMultiScale(image, winStride=(4,4),padding=(8,8),scale=1.05) 
	#Detect objects of different sizes for body detection ^
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converts image colorspace to another in this case gray
	faces = faceCascade.detectMultiScale(gray, 1.3, 5) #This will detect objects of different sizes
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs = None, overlapThresh = 0.65)
	for(xA, yA, xB, yB) in pick: #Iterates through non_max_supression
            cv2.rectangle(image, (xA, yA), (xB,yB), (0,225, 0), 2) #This will place a box over the users body
	for(x, y, w, h) in faces: #This will iterate through haarcascade
            cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2) #This will return a green box around users faces
        ret, jpeg = cv2.imencode('.jpg', image) #Makes the a jpg image
        return jpeg.tobytes() #Returns the jpeg image!
