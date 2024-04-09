from ultralytics import YOLO
import cv2

#yolo basics 

model = YOLO("yolov8n.pt")
results = model(r"D:\10_PYTHON PROJECTS\ONLINE_FACE_DETECTION\Running Yolo\images2.jpg",show=True)
cv2.waitKey(0)