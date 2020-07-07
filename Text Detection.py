import cv2
import pytesseract  # only accept RGB values

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(r"C:\Users\windows 10\Desktop\OpenCV Image\Images\test.jpeg")
resized = cv2.resize(img, (int(img.shape[1]/1),int(img.shape[0]/1)))
img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
img1 = img.copy()

print(pytesseract.image_to_string(img))


#*******(Detecting Characters)******
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)   # bounding box to each letter
for b in boxes.splitlines():
    b = b.split(" ")
    #print(b)

    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1) 
    cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_ITALIC,0.9,(0,255,0),2)



#*******(Detecting Words)******
boxes = pytesseract.image_to_data(img1)   
print(boxes) # 0th column contain heading

for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        #print(b)

        if len(b)==12: # only b with 12 attributes contain our text in last column
            x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),1) 
            cv2.putText(img1,b[11],(x+5,y-3),cv2.FONT_ITALIC,0.9,(0,255,0),2)






cv2.imshow("Characters", img)
cv2.imshow("Words", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
