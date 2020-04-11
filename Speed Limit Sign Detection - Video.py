#   Speed Limit Sign Detection
#   Code By Sippawit Thammawiset

import cv2
import imutils
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import os

capture = cv2.VideoCapture(0)
_, video = capture.read()

try:
    if not os.path.exists('text_detected/text_detected.png'):
        cv2.imwrite('text_detected/text_detected.png', video)
except OSError:
    print ('Error: Creating text_detected.png')

while True:
    _, video = capture.read()
    video = imutils.resize(video, width=800)
    height, width, _ = video.shape
    mask = np.zeros((height, width, _), np.uint8)

    gray = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(blur, 170, 200)

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
    cv2.drawContours(mask, contours, -1, (0, 255, 0), -1)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        if  20 > len(approx) >= 15:
            circle_detected = video * mask
            gray = cv2.cvtColor(circle_detected, cv2.COLOR_BGR2GRAY)
            blur = cv2.bilateralFilter(gray, 11, 17, 17)
            _, thresh = cv2.threshold(blur, 90, 255, cv2.THRESH_BINARY)        #   You have to change the value of Threshold here as well if a result image is too bright.
            cv2.imshow('THRESHOLD', thresh)
            cv2.imwrite('text_detected/' + str('text_detected') + '.png', thresh)

            text_detected_locate = Image.open('text_detected/' + str('text_detected') + '.png')
            text_detected = pytesseract.image_to_string(text_detected_locate, config='-l eng+tha')
            if text_detected == '':
                text_detected = 'NO DETECTED!'
                video = cv2.putText(video, 'SPEED LIMIT DETECTED: ' + text_detected, (20, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                video = cv2.putText(video, 'SPEED LIMIT DETECTED: ' + text_detected + str(' KM/H'), (20, 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('VIDEO', video)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()