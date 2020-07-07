import numpy as np
import cv2
import time

    # *******for my blue tshirt*******
    #lower_blue = np.array([92,118,85])
    #upper_blue = np.array([109,255,255])


cap = cv2.VideoCapture(0)

time.sleep(2)
background = 0               #capturing background
for i in range(30):
    ret, background = cap.read()

#capturing image

while(cap.isOpened()):
    ret, img = cap.read()
    
    if not ret:
        break
        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([92,118,85])
    upper_red = np.array([109,255,255])
    mask1 = cv2.inRange(hsv , lower_red , upper_red)

    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=2)
    """
    lower_red = np.array([92,111,0])
    upper_red = np.array([118,255,103])
    mask2 = cv2.inRange(hsv , lower_red , upper_red)
    
    mask1 = mask1 + mask2 #OR
    
        
    #mask2=cv2.morphologyEx(mask1, cv2.MORPH_DILATE ,np.ones((3,3) , np.uint8) , iterations=1)
    """   
    mask2 = cv2.bitwise_not(mask1)
    
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    
    final_output = cv2.addWeighted(res1 , 1, res2 , 1, 0)
    
    
    cv2.imshow('Jatin' , final_output)
    k=cv2.waitKey(5)
    if k==ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
