import cv2
import numpy as np

# for "g.jpg" with orange cake set values 0,179,207,255,202,255
# for "b.jpg" with orange shirt set values 171,179,95,255,103,255
# for "7.jpg" with orange car set values 10,179,58,255,164,255
# for "2.jpg" with white snow set values 0,179,0,255,219,255
# for "3.jpg" with white snow set values 179,155,3,29,152,255

def empty(a):
    pass


cv2.namedWindow("Track Bar")
cv2.resizeWindow("Track Bar",640,200)
cv2.createTrackbar("Hue Min","Track Bar",0,179,empty)
cv2.createTrackbar("Hue Max","Track Bar",179,179,empty)
cv2.createTrackbar("Sat Min","Track Bar",0,255,empty)
cv2.createTrackbar("Sat Max","Track Bar",255,255,empty)
cv2.createTrackbar("Val Min","Track Bar",0,255,empty)
cv2.createTrackbar("Val Max","Track Bar",255,255,empty)


while True:
    img = cv2.imread (r"C:\Users\windows 10\Desktop\OpenCV Image\Images\green.jpg",1)
    resized = cv2.resize(img, (int(img.shape[1]/2.5),int(img.shape[0]/2.5))) 
    imgHSV = cv2.cvtColor(resized,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","Track Bar")
    h_max = cv2.getTrackbarPos("Hue Max","Track Bar")
    s_min = cv2.getTrackbarPos("Sat Min","Track Bar")
    s_max = cv2.getTrackbarPos("Sat Max","Track Bar")
    v_min = cv2.getTrackbarPos("Val Min","Track Bar")
    v_max = cv2.getTrackbarPos("Val Max","Track Bar")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max]) 
    mask = cv2.inRange(imgHSV,lower,upper) # filter out image of that color (keep it white)

    imgResult = cv2.bitwise_and(resized,resized,mask=mask) #show our picked color range

    cv2.imshow("jatin", resized)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Final", imgResult)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
    