import cv2

img = cv2.imread (r"C:\Users\windows 10\Desktop\OpenCV Image\Images\b.jpg",1)

bounding_box = cv2.selectROI("Tracking",img,False)
print(bounding_box)

#print(img.shape) prints height first then width

resized = cv2.resize(img, (int(img.shape[1]/2.5),int(img.shape[0]/2.5))) 
imgBlur = cv2.GaussianBlur(resized,(9,9),0)
imgCanny = cv2.Canny(resized,120,120)
imgCropped = resized[0:200, 200:400] # height first then width

cv2.line(resized,(0,0),(100,100),(0,255,0),2)
cv2.circle(resized,(100,100),50,(255,0,0),2)
cv2.rectangle(resized,(0,0),(100,100),(0,0,255),2)


cv2.imshow("jatin", resized)
cv2.imshow("blur", imgBlur)
cv2.imshow("canny", imgCanny)
cv2.imshow("cropped", imgCropped)
cv2.imshow("img", img)
cv2.waitKey(0)


