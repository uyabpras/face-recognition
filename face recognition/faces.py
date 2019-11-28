import cv2
import numpy as np
import pickle
import tweepy
import tweet

face_cascade = cv2.CascadeClassifier('opencv-files/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

labels = {"person_name": 0}
with open("labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

vc = cv2.VideoCapture(0) #command open webcam


while True:
    ret, frame = vc.read() #read webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #change color to gray
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5) #scaling face movement
    for (x, y, w, h) in faces:
        #print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf >= 10 and conf <= 75:
            #print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)
        color = (0, 255, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(20)
	if labels[id_] == 'zboss':
	    owner = labels[id_]
	    tweet.posting_owner(owner)
    if key == 27:
	    tweet.posting()
	    break

file = open("recognizer.txt", "w")
file.write(name+"\n")

cv2.destroyWindow("frame")
vc.release() #open webcam
