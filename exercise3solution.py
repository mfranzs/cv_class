# Press CTRL + B to run this file (Select "Python")

def process_image(img, width, height):
    top_left_corner_x = 999
    top_left_corner_y = 999
    bottom_right_corner_x = -999
    bottom_right_corner_y = -999

    for x in range(width):
        for y in range(height):
            pixel = img[y][x]
            b, g, r = pixel

            if r > b + 40 and r > g + 40:

                if x < top_left_corner_x:
                    top_left_corner_x = x
                if y < top_left_corner_y:
                    top_left_corner_y = y

                if x > bottom_right_corner_x:
                    bottom_right_corner_x = x
                if y > bottom_right_corner_y:
                    bottom_right_corner_y = y

                img[y][x] = (0, 0, 255)

    cv2.circle(img, center=(top_left_corner_x, top_left_corner_y), radius=5, color=(0,0,0), thickness=-1)
    cv2.circle(img, center=(bottom_right_corner_x, bottom_right_corner_y), radius=5, color=(0,0,0), thickness=-1)
    cv2.rectangle(img, pt1=(top_left_corner_x, top_left_corner_y), pt2=(bottom_right_corner_x, bottom_right_corner_y), color=(0,0,0))

    return img


# Be careful changing things below this line! =============================

import numpy as np
import cv2

cap = cv2.VideoCapture(0) # Open a new video capture

while(True):
    # Capture frame-by-frame
    ret, img = cap.read()
    # Rescale the image for speed
    SCALE = .3
    img = cv2.resize(img,None,fx=SCALE, fy=SCALE)
    height, width, _ = img.shape

    # Run the image through processing
    img = process_image(img, width, height)

    # Rescale the image back to size
    # img = cv2.resize(img,None,fx=1/SCALE, fy=1/SCALE)

    # Display the resulting frame
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()