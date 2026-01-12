import cv2
import numpy as np

cap = cv2.VideoCapture(0)   

bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=True
)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

print("Press 'q' to quit")


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break


    fg_mask = bg_subtractor.apply(frame)


    _, fg_mask = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)


    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
    fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_DILATE, kernel)

    contours, _ = cv2.findContours(
        fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )


    for cnt in contours:
        if cv2.contourArea(cnt) > 1000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Motion Detected",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (0, 255, 0), 2)


    cv2.imshow("Original Frame", frame)
    cv2.imshow("Foreground Mask", fg_mask)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
