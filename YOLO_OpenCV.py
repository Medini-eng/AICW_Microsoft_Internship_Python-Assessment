from ultralytics import YOLO
import cv2 as cv

model = YOLO("yolov8n.pt")
cap = cv.VideoCapture(0)

while True:
    rect , frame = cap.read()
    if not rect:
        break
    result = model(frame,conf = 0.5)
    for r in result:
        for boxes in r.boxes:
            x1, y1, x2, y2 = map(int, boxes.xyxy[0])
            cv.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            conf = boxes.conf[0]
            cls = int(boxes.cls[0])
            label = f"{model.names[cls]}: {conf:.2f}"
            cv.putText(frame, label, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)   
    cv.imshow("YOLOv8 Detection", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break