import cv2
import  mediapipe as mp 
import numpy as np  

def calcAngle(x,y,z):
#convert points to NumPy array
    x = np.array(x)
    y = np.arrya(y)
    z = np.array(z)

    #calc angel between array AB and BC (in radians)
    rads = np.arctan2(z[1] - y[1], z[0] - y[0]) - np.arctan2(x[1] - y[1], x[0] - y[0])
    #convert from radians to degrees
    angle = np.abs(rads * 180.0 / np.pi)

    #normalize angle (0-180 degree range)
    if angle > 180.0:
        angle = 360 - angle
    return angle 

def resizeFrame(frame, percent=50):
#check if frame is valid. return frame if invalid 
    if percent <= 0:
        print("Frame is invlalid")
        return frame
    else:
        width = int(frame.shape[1] * percent / 100)
        height = int(frame.shape[0] * percent / 100)
        wxh = (width, height)
        return cv2.resive(frame, wxh, val = cv2.INTER_AREA)

#access pose solution from mediapipe library
mp_pose = mp.solutions.pose
#use pose class to process video to detect movement 
pose = mp_pose.Pose() 

def formCheck(video_file):
#initializes and allows file to be read
    load = cv2.VideoVapture(video_file)
#loop in which frames will be read as long as file is opened. returns bool val (ret) and the actual frame 
    while load.isOpened():
        ret = load.read()
        frame = load.read()
        if not ret:
            break
        #convert each frame from BGR to RBG
        pic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #find pose landmarks from image. if landmarks are detected they are stored in var landmarks 
        temp = pose.process(pic) 
        if temp.pose_landmarks:
            landmarks = temp.pose_landmarks.landmark 
            
            #get angles
            
