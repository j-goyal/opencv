import cv2
import numpy as np

def getContour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>700:            
            peri = cv2.arcLength(cnt,True)  # curve length to help approx corners 
            approx = cv2.approxPolyDP(cnt,0.01*peri,True) # gives corner points coordinates for each shape
            cv2.drawContours(imgContour,approx,-1,(255,0,255),7) # Pink dots (draw only corner points)
            objCorners = len(approx)
            print(objCorners)

            x, y, w, h = cv2.boundingRect(approx) # create bounding rectangle around shape
            #print(w,h)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(255,0,0),1) # blue

            # now start categorize object

            if objCorners==3:
                objType = "Tri"
            elif objCorners == 4:
                aspRatio = w/h
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objType = "Square"
                else:
                    objType = "Rectangle"
            elif objCorners > 10 :
                objType = "Circle"
            else:
                objType = "None"

            cv2.putText(imgContour,objType,(x+w//2-25 , y+h//2),cv2.FONT_ITALIC,0.5,(0,0,0),2)




img = cv2.imread(r"C:\Users\windows 10\Desktop\OpenCV Image\Images\11.jpg")

resized = cv2.resize(img, (int(img.shape[1]/2.5),int(img.shape[0]/2.5)))
imgContour = resized.copy()
imgGray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
#imgDilate = cv2.dilate(imgCanny,np.ones([3,3]),iterations=1) # make edges thicker
#imgErode = cv2.erode(imgDilate,np.ones([3,3]), iterations=1) # make edges thinner


getContour(imgCanny)

cv2.imshow("jatin", imgGray)
cv2.imshow("blur", imgBlur)
cv2.imshow("canny", imgCanny)
cv2.imshow("contours", imgContour)
#cv2.imshow("Erode", imgErode)
#cv2.imshow("Dilate", imgDilate)

cv2.waitKey(0)
cv2.destroyAllWindows()