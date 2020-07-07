import cv2, time

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')

# for capturing whole video we use for loop
a=1
while True:
    a=a+1
    check, frame = video.read()
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
        cv2.putText(frame,"Face",(x,y-6),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
            cv2.putText(roi_color,"Eye",(ex,ey-6),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)


    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1) # generate frame every 1 millisec

    if key == ord('q'):  # on pressing q it quits the window
        break

print(a)
video.release()
cv2.destroyAllWindows()


"""
check, frame = video.read()

#print(check) # return true if python is able to read video capture 
#print(frame)
time.sleep(2)
cv2.imshow("Capturing", frame) #capture first frame only 
cv2.waitKey(0)

video.release()
cv2.destroyAllWindows()
"""