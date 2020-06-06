import os
import time
import random
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,help="path to the folder wich contains image files")
ap.add_argument("-w", "--width", type=int,help="width of the video resolution")
ap.add_argument("-he", "--height", type=int,help="height of the video resolution")
ap.add_argument("-f", "--fps", type=int,help="fps of the video depending on the number of frames")
ap.add_argument("-o", "--output", type=str, default='output', \
 help="name of the output file without extension")
args = vars(ap.parse_args())

input_path = args["input"]
#Check whether the folder containing images exist or not
exists = os.path.isdir(input_path)
if not exists:
    print("Please check whether the input folder exists or not")
    exit()

#If name of the output video file is not defined or if the video file already exists then create a new file
if not args["output"] or os.path.isfile(args["output"]+'.mp4'):
    num = random.randint(0,100)
    path = 'output'+str(num)+'.mp4'
    print("Output file name is not specified or the name already exists.So,creating a file named ",path)
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    writer = cv2.VideoWriter(path+'.mp4', fourcc, args["fps"],(args["width"], args["height"]), True)
else:
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    writer = cv2.VideoWriter(args["output"]+'.mp4', fourcc, args["fps"],(args["width"], args["height"]), True)


for root, directories, files in os.walk(args["input"]):
    for file in files:
        #Check for image files with .png , .jpg or .jpeg extension
        if '.jpg' or '.png' or '.jpeg' in file:
            dim = (args["width"], args["height"])
            image = cv2.imread(os.path.join(args["input"],file))
            #resize the image based on video resolution
            resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
            #file = cv2.resize(file,(int(args))
            writer.write(resized)

