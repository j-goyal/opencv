import cv2
import numpy as np
 
circles = np.zeros((4,2),np.int)  # to store 4 cordinates of image
counter = 0
 
def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter + 1


 
img = cv2.imread(r"C:\Users\windows 10\Desktop\OpenCV Image\Images\card2.jpg")
#img = cv2.resize(img,(800,600))
imgCopy = img.copy()

while True:
    if counter == 4:
        width, height = 250,350 # normally for a playing card
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("Output Image ", imgOutput)

    for x in range (0,4):
        cv2.circle(imgCopy,(circles[x][0],circles[x][1]),4,(255,0,0),cv2.FILLED)
        

    #cv2.imshow("Original Image ", img)
    cv2.imshow("Copy Image", imgCopy)
    cv2.setMouseCallback("Copy Image", mousePoints)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break