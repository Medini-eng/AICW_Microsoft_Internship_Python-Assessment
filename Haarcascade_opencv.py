import cv2 as cv
facw_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv.VideoCapture(0)

while True:
    rect, frame = cap.read()
    if not rect:
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = facw_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv.imshow("Video Feed", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break