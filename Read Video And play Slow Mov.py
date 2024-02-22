import cv2
import numpy as np
cap=cv2.VideoCapture(r"C:\Users\cakeo\Downloads\( 4K ) Royal Enfield Continental GT 650 🥵🔥_ switch edits.mp4")
if(cap.isOpened()==False):
    print("Error in Opening Video")

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        cv2.imshow('Frame',frame)
        if cv2.waitKey(250)&0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
