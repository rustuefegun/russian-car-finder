import cv2 as cv
import serial

cascade = cv.CascadeClassifier(r'C:\\Users\\User\\Desktop\\opencv\\haarcascade_russian_plate_number.xml')
#smile_cascade = cv.CascadeClassifier('smile.xml')
serport = serial.Serial("COM4", baudrate=9600, timeout=1)

cap = cv.VideoCapture(1)
cap.set(3,240)
cap.set(4,480)

while True:
    _,img = cap.read()
    
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray, 1.1, 6)
    for(x, y, w, h) in faces:
        cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        #smile=smile_cascade.detectMultiScale(gray, scaleFactor=1.8, minNeighbors=16)
        #for(x, y, w, h) in smile:
        #    img=cv.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
            

    cv.imshow('img', img)
    if(len(faces)==0):
        serport.write(b'c')
    elif(len(faces)>0):
        serport.write(b'b')



    if cv.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv.destroyAllWindows
