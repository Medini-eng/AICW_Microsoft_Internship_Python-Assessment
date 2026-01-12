import cv2
import numpy as np

img = cv2.imread(r"C:\Users\medin\Desktop\Demo_OpenCV\1_qQbo4YRT32LfyXRWdR1irQ.png")
img = cv2.resize(img, (500, 400))

hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

cv2.namedWindow("HLS Adjust")

def nothing(x):
    pass

cv2.createTrackbar("Hue", "HLS Adjust", 0, 179, nothing)
cv2.createTrackbar("Lightness", "HLS Adjust", 0, 255, nothing)
cv2.createTrackbar("Saturation", "HLS Adjust", 0, 255, nothing)

while True:
    h = cv2.getTrackbarPos("Hue", "HLS Adjust")
    l = cv2.getTrackbarPos("Lightness", "HLS Adjust")
    s = cv2.getTrackbarPos("Saturation", "HLS Adjust")

    h_channel, l_channel, s_channel = cv2.split(hls)

    h_channel = cv2.add(h_channel, h)
    l_channel = cv2.add(l_channel, l)
    s_channel = cv2.add(s_channel, s)

    hls_modified = cv2.merge([h_channel, l_channel, s_channel])
    result = cv2.cvtColor(hls_modified, cv2.COLOR_HLS2BGR)

    cv2.imshow("HLS Adjust", result)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
