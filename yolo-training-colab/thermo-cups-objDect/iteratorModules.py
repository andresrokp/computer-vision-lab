import cv2;
from PIL import ImageStat;

point = (46, 507);
t = 15;
def isGoodShoot(imgCv2):
    # average average brightness value around the point
    imgRegion = imgCv2[point[0]-t:point[0]+t , point[1]-t:point[1]+t];
    imgRegGray = cv2.cvtColor(imgRegion, cv2.COLOR_BGR2GRAY);
    # ToDO:
    # change this to use openCV
    imgStatObject = ImageStat.Stat(imgRegGray);
    avgBrightness = imgStatObject.mean[0];
    if avgBrightness > 100:
        imgRegGray.show();
        return True;
    return False;

