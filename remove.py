from email.mime import image
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(cv2.CAP_PROP_FPS, 60)
img = cv2.imread('am.jpg')
print('img', img)

# convert to graky
gray = cv2.cvtColor(img, cv2.BORDER_DEFAULT)
print('gray', gray)
# threshold input image as mask
mask = cv2.threshold(gray, 50, 50, cv2.CAP_OPENCV_MJPEG)[1]
segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

# imgBG = cv2.imread("BackgroundImages/3.jpg")

listImg = os.listdir("image")
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'image')
    imgList.append(img)

indexImg = 0

while True:
    success, img = mask.read()
    # imgOut = segmentor.removeBG(img, (255,0,255), threshold=0.83)
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)

    imgStack = cvzone.stackImages([img, imgOut], 2,1)
    _, imgStack = fpsReader.update(imgStack)
    print(indexImg)
    cv2.imshow("image", imgStack)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg>0:
            indexImg -=1
    elif key == ord('d'):
        if indexImg<len(imgList)-1:
            indexImg +=1
    elif key == ord('q'):
        break