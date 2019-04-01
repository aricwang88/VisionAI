import cv2
import numpy as np

#cap = cv2.VideoCapture("rtsp://192.168.1.3:8554/live") #http://172.16.1.89:8080/?action=stream") #0)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_BUFFERSIZE,1)
cap.set(3, 1280)
cap.set(4, 720)

template = cv2.imread("../face.png",0)
w, h = template.shape[::-1]

while True:
    ret,frame = cap.read()
    big_frame = cv2.resize(frame, (1280,720))

    img_gray = cv2.cvtColor(big_frame, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= 0.7)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(big_frame, pt, (pt[0]+w, pt[1]+h), (7,249,151),1)
    
    #cv2.imshow("GRAY", img_gray)
    cv2.imshow("frame", big_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

