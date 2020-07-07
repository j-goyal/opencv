import cv2, time
# pip install opencv-contrib-python --user


# create a tracker for our object. There are many trackers available
tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']

#tracker = cv2.TrackerMOSSE_create() # greater speed, low accuracy 
tracker = cv2.TrackerCSRT_create() # low speed, high accuracy
#tracker = cv2.TrackerKCF_create()

video = cv2.VideoCapture(0)
success, img = video.read()

bounding_box = cv2.selectROI("Tracking",img,False) # return tuple

tracker.init(img, bounding_box)


def drawBox(img, bounding_box):
    x, y, w, h = int(bounding_box[0]), int(bounding_box[1]), int(bounding_box[2]), int(bounding_box[3])
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,255), 3, 1)
    cv2.putText(img,"Tracking",(50,75),cv2.FONT_ITALIC,0.7,(0,255,0),2)


while True:
    timer = cv2.getTickCount()
    success, img = video.read()

    success, bounding_box = tracker.update(img)
    
    if success==True:
        drawBox(img,bounding_box)
    else:
        cv2.putText(img,"Lost",(50,75),cv2.FONT_ITALIC,0.7,(0,0,255),2)
    
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)

    cv2.putText(img,str(int(fps)),(50,50),cv2.FONT_ITALIC,0.7,(0,0,255),2)

    cv2.imshow("Capturing", img)
    key = cv2.waitKey(1) # generate frame every 1 millisec

    if key == ord('q'):  # on pressing q it quits the window
        break