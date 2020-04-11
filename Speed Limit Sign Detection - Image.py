#   Speed Limit Sign Detection
#   Code By Sippawit Thammawiset

import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import os

image = cv2.imread('img/1.jpg')
image = imutils.resize(image, width=1024, height=800)
height, width, _ = image.shape
mask = np.zeros((height, width, _), np.uint8)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(blur, 170, 200)

contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
cv2.drawContours(mask, contours, -1, (0, 255, 0), -1)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
    if  20 > len(approx) >= 10:
        circle_detected = image * mask
        gray = cv2.cvtColor(circle_detected, cv2.COLOR_BGR2GRAY)
        blur = cv2.bilateralFilter(gray, 11, 17, 17)
        _, thresh = cv2.threshold(blur, 110, 255, cv2.THRESH_BINARY)        #   You have to change the value of Threshold here as well if a result image is too bright.
        cv2.waitKey(0)
        cv2.imwrite('text_detected/' + str('text_detected') + '.png', thresh)

text_detected_locate = Image.open('text_detected/' + str('text_detected') + '.png')
text_detected = pytesseract.image_to_string(text_detected_locate, config='-l eng+tha')
print ('SPEED LIMIT DETECTED: ' + str(text_detected) + ' KM/H')
image = cv2.putText(image, 'SPEED LIMIT DETECTED: ' + text_detected + str(' KM/H'), (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imshow('IMAGE', image)
circle_detected = imutils.resize(circle_detected, width=400)
cv2.imshow('DETECTED', circle_detected)
cv2.waitKey(0)