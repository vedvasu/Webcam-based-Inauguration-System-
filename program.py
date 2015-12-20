##############################################
import numpy as np
import cv2
import serial
import time                                  # impot time for working with time.sleep() statement
#############################################
#initialising Camera, 1 for external camera, 0 for laptop webcam
cap = cv2.VideoCapture(1)

#############################################
Program Processing
#############################################
while(1):
    ## Read the image
    ret, img = cap.read()
    lenght, width, color = img.shape
    
    #cv2.circle(img,(l/2,w/2), 5, (0,0,255), -1)     #uncomment this for viewing the center point
    
    B,G,R = img[l/2,w/2]                             # I have used the mid point of the frame for testing light intensity
    
    if B>50:                                         # for least light the R,G,B values are 0,0,0 (Perfectly black)
                                                     # 50 is used as zero error as perfect black never happens
        ser = serial.Serial(2,timeout=1)
        ser.baudrate = 9600                          #initiating the zigbee module serial port
        
        ser.write("8")                               #in the embedded code of the robot, ASCII 8 is used for moving forward
        ser.close()                                  #port is closed after the operation
    else:
        
        ser = serial.Serial(2,timeout=1)             #initiating the zigbee module serial port
        ser.baudrate = 9600
        
        ser.write("5")                              #in the embedded code of the robot, ASCII 8 is used for moving forward
        ser.close()                                 #port is closed after the operation
        
    cv2.imshow('image',img)                     # for displaying image for checking purpose
    
    if cv2.waitKey(1) == 27:
        break

############################################
## Close and exit
cv2.destroyAllWindows()
############################################
