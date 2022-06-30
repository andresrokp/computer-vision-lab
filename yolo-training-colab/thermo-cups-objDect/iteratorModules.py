import cv2;

point = [46, 507];
t = 15;
def isGoodShoot(imgCv2):
    # average average brightness value around the point
    imgCrop = imgCv2[point[0]-t:point[0]+t , point[1]-t:point[1]+t];
    imgCropGray = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY);
    avgBrightness = imgCropGray.mean();
    if avgBrightness > 100:
        return True;
    return False;

