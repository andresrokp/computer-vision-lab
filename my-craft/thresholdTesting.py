import cv2
import myvars

# open an image .jpg
img = cv2.imread(f'{myvars.photopath}{myvars.img1}')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)


cv2.imshow("Color Frame", cv2.resize(img, (0, 0), fx=0.15, fy=0.15))
cv2.imshow("Gray Frame", cv2.resize(gray, (0, 0), fx=0.15, fy=0.15))
cv2.imshow("Blur Frame", cv2.resize(blur, (0, 0), fx=0.15, fy=0.15))
cv2.imshow("Thresh Frame", cv2.resize(thresh, (0, 0), fx=0.15, fy=0.15))


key = cv2.waitKey(0)