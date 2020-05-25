import os
import time
import random
import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,help="path to input video file")
ap.add_argument("-o", "--output", type=str, default='output', \
 help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

#If input file name is not specified then it tries to capture frames from webcam
if not args["input"]:
    print("Trying to capture the frames from webcam")
    cap = cv2.VideoCapture(0)
else:
    input_path = args["input"]
    #Check whether the video file exists or not
    exists = os.path.isfile(input_path)
    if not exists:
        print("Please check the input video file path")
        exit()
    cap = cv2.VideoCapture(args["input"])


#check whether the location to store the output is specified or not.
#If not specified or the folder does not exist then create a new folder to save frames
if not args["output"] or not os.path.exists(args["output"]):
    num = random.randint(0,100)
    path = 'output'+str(num)
    print("Output folder does not exist or not specified,creating a folder named '",path,"'and saving frames")
    os.makedirs(path)
else:
    path = args["output"]

frame_number = 1

while True:
    #Extract frames
    ret, frame = cap.read() 
    #Check whether the we reached last frame
    if not ret:
        print('Done...')
        break
    if frame_number==1:
        print("Extracting frames")
    #Add number to each extracted frame
    name = os.path.join(path,'frame'+str(frame_number)+'.png')
    cv2.imwrite(name,frame)
    frame_number+=1


