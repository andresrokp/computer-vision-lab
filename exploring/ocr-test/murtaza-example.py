from cv2 import split
import pytesseract as pts
import cv2


print("-\n--\n---\n----\n-----\n----\n---\n--\n-")

pts.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

img = cv2.imread("text in img.png")
imgHeight, imgWidth,_ = img.shape
# cv2.cvtColor(img, cv2.COLOR_BGR2BGR)

print(pts.image_to_string(img))
boxesTxt = pts.image_to_boxes(img) 

for b in boxesTxt.splitlines():
    x1,y1,x2,y2 = [int(i) for i in b.split(' ')[1:5]]
    print(b)
    cv2.rectangle(img, (x1,imgHeight-y1), (x2,imgHeight-y2), (0,0,255),2)
    cv2.putText(img,b[0],(x1,imgHeight-y2-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),1)
    

dataGrid = pts.image_to_data(img)
print(dataGrid)

cv2.imshow("img", img)

cv2.waitKey(0)

print("\n\n- - -\nOK mackey\n- - -")




# image_to_boxes
# splitlines
# split
# rectangle(img,(x1,y1),(x2,y2),(r.g.b),thick)
