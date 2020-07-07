import cv2

#img = cv2.imread (r"C:\Users\windows 10\Desktop\1.jpg",0)

#print(img.shape)

#resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))# opposite arguments
#print(resized.shape)

#cv2.imshow("jatin", resized)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r'haarcascade_eye.xml')
img = cv2.imread(r"C:\Users\windows 10\Desktop\OpenCV Image\Images\c.jpg",1)

#print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=2)

#print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
    roi_gray = gray_img[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

    #cv2.imshow("jsojl", roi)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

#resized = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))




cv2.imshow("jatin", img)
cv2.waitKey(0)
cv2.destroyAllWindows()