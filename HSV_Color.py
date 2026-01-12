import cv2
import numpy as np


img = cv2.imread(r"C:\Users\medin\Desktop\Demo_OpenCV\1_qQbo4YRT32LfyXRWdR1irQ.png")
img = cv2.resize(img, (500, 400))
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow("HSV Adjust")
def nothing(x):
    pass
cv2.createTrackbar("Hue", "HSV Adjust", 0, 179, nothing)
cv2.createTrackbar("Saturation", "HSV Adjust", 0, 255, nothing)
cv2.createTrackbar("Value", "HSV Adjust", 0, 255, nothing)

while True:
    h = cv2.getTrackbarPos("Hue", "HSV Adjust")
    s = cv2.getTrackbarPos("Saturation", "HSV Adjust")
    v = cv2.getTrackbarPos("Value", "HSV Adjust")
    h_channel, s_channel, v_channel = cv2.split(hsv)
    h_channel = cv2.add(h_channel, h)
    s_channel = cv2.add(s_channel, s)
    v_channel = cv2.add(v_channel, v)
    hsv_modified = cv2.merge([h_channel, s_channel, v_channel])
    result = cv2.cvtColor(hsv_modified, cv2.COLOR_HSV2BGR)

    cv2.imshow("HSV Adjust", result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
