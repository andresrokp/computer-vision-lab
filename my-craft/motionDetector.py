import cv2
 
# Assigning our static_back to None
static_back = None
 
# Capturing video
video = cv2.VideoCapture(0)

# screenshot counter
ssc = 0;

# Infinite while loop to treat stack of image as video
while True:
    # Reading frame(image) from video
    check, frame = video.read()

    print(type(frame))
 
    # Converting color image to gray_scale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    # Converting gray scale image to GaussianBlur
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
    # In first iteration we assign the value
    # of static_back to our first frame
    if static_back is None:
        static_back = gray
        continue
 
    # Difference between background and the first blurred-grayed frame
    diff_frame = cv2.absdiff(static_back, gray)
 
    # generate a threshold image from the difference image. 
    thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)
 
    # Spoting countours of the threshold image (...perimeter of things that moved)
    cnts,_ = cv2.findContours(thresh_frame.copy(),
                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
    for contour in cnts:
        # ignores small countours (...or movements)
        if cv2.contourArea(contour) < 10000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        # making rectangles around the big countours (...moving object)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
 
    # Displaying original frame plus the rectangles
    cv2.imshow("Color Frame", frame)
 
    key = cv2.waitKey(1)
    # if q is pressed, then exit
    if key == ord('q'):
        break
    
    if key == ord('s'):
        ssc += 1;
        cv2.imwrite(f"screenshots/screenshot{ssc}.png", frame)


video.release()
cv2.destroyAllWindows()