import cv2
from cvzone.HandTrackingModule import HandDetector

width, height = 1280, 720

cap = cv2.VideoCapture(0)

cap.set(3, width)
cap.set(4, height)


while True:
    success, img = cap.read()

    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break