import cv2
import numpy as np
import cvzone
from cvzone.
import os

# load image
img = cv2.imread('am.jpg')
print('img', img)

# convert to graky
gray = cv2.cvtColor(img, cv2.BORDER_DEFAULT)
print('gray', gray)
# threshold input image as mask
mask = cv2.threshold(gray, 50, 50, cv2.CAP_OPENCV_MJPEG)[1]
print('maskdd', mask)
# negate mask
mask = 50 - mask
print('mask 105', mask)
# apply morphology to remove isolated extraneous noise
# use borderconstant of black since foreground touches the edges
kernel = np.ones((1,1), np.uint8)
print('kernel205', kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
print('masksss', mask)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
print('maskssa', mask)
# anti-alias the mask -- blur then stretch
# blur alpha channel
mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2, borderType = cv2.BORDER_DEFAULT)
print('maskt', mask)
# linear stretch so that 127.5 goes to 0, but 255 stays 255
mask = (2*(mask.astype(np.float32))-50.0).clip(0,50).astype(np.uint8)
print('masksssst', mask)
# put mask into alpha channel
result = img.copy()
print('result', result)
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
print('resultss2', result)
# result[:, :, 3] = mask
print('resultss3', result)
# save resulting masked image
cv2.imwrite('person_transp_bckgrnd.png', result)
imagebg=
# display result, though it won't show transparency
cv2.imshow("INPUT", img)
cv2.imshow("GRAY", gray)
cv2.imshow("MASK", mask)
cv2.imshow("RESULT", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

