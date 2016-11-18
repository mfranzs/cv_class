import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()
    SCALE = .4
    img = cv2.resize(img,None,fx=SCALE, fy=SCALE)

    height, width, _ = img.shape

    for x in range(width):
		for y in range(height):
			pixel = img[y][x]
			b, g, r = pixel

			if b == max(b, g, r):
				img[y][x] = (255, 0, 0)

			if g == max(b, g, r):
				img[y][x] = (0, 255, 0)

			if r == max(b, g, r):
				img[y][x] = (0, 0, 255)

    # Display the resulting frame
    # img = cv2.resize(img,None,fx=1/SCALE, fy=1/SCALE)

    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()