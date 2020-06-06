import os
import time
import random
import cv2
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,help="path to input video file")
ap.add_argument("-o", "--output", type=str,help="name of the output video file")
args = vars(ap.parse_args())


input_path = args["input"]
#Check whether the video file exists or not
exists = os.path.isfile(input_path)
if not exists:
    print("Please check the input video file path")
    exit()
cap = cv2.VideoCapture(args["input"])

fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


#check whether the location to store the output is specified or not.
#If not specified or if it already exists then create a new video file
if not args["output"] or os.path.isfile(args["output"]+'.mp4'):
    num = random.randint(0,100)
    path = 'output'+str(num)+'.mp4'
    print("Output file name is not specified or the name already exists.So,creating a file named ",path)
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    writer = cv2.VideoWriter(path+'.mp4', fourcc, fps,(width, height), True)
else:
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    writer = cv2.VideoWriter(args["output"]+'.mp4', fourcc, fps,(width, height), True)

frame_number = 0
frames = list()
flag = False

while True:
    #If we have reached the end of the frame,then start arranging frames in reverse order
    if flag:
        for index in range(frame_number-1, -1, -1):  
            writer.write(frames[index])
        break
    #Extract frames
    ret, frame = cap.read()
    if not ret:
        flag = True
        continue
    frames.append(frame) 
    frame_number+=1

