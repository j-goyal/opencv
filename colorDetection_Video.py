import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver



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


video = cv2.VideoCapture(0)
video.set(3,340)
video.set(4,480)

# for capturing whole video we use for loop
while True:
    check, img = video.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min","Track Bar")
    h_max = cv2.getTrackbarPos("Hue Max","Track Bar")
    s_min = cv2.getTrackbarPos("Sat Min","Track Bar")
    s_max = cv2.getTrackbarPos("Sat Max","Track Bar")
    v_min = cv2.getTrackbarPos("Val Min","Track Bar")
    v_max = cv2.getTrackbarPos("Val Max","Track Bar")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max]) 
    mask = cv2.inRange(imgHSV,lower,upper) # filter out image of that color (keep it white)

    imgResult = cv2.bitwise_and(img,img,mask=mask) #show our picked color range

    # cv2.imshow("jatin", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Final", imgResult)

    # ======== Call stack fun to show images together
    imgStack = stackImages(1,([mask,imgResult],[img,imgHSV]))
    cv2.imshow("ImageStack",imgStack)

    key = cv2.waitKey(1)

    if key == ord('q'):  # on pressing q it quits the window
        break

video.release()
cv2.destroyAllWindows()

