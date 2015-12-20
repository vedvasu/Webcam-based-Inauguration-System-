##############################################
## Import OpenCV
import numpy as np
import cv2
import serial
import time                                                          # impot time for working with time.sleep() statement
#############################################
cap = cv2.VideoCapture(1)
while(1):
    ## Read the image
    ret, img = cap.read()
    #cv2.circle(img,(320,240), 5, (0,0,255), -1)
    B,G,R = img[240,320]
    if B>50:
        ser = serial.Serial(2,timeout=1)
        ser.baudrate = 9600
        ser.write("8")
        print "moving"
        ser.close()
    else:
        ser = serial.Serial(2,timeout=1)
        ser.baudrate = 9600
        ser.write("5")
        ser.close()
        
    
    print B,G,R
    cv2.imshow('image',img)
    if cv2.waitKey(1) == 27:
        break

############################################
## Close and exit
cv2.destroyAllWindows()
############################################
